import mimetypes
from rdfcrate import sdo, roc
from rdfcrate.context_graph import EntityArgs
from rdfcrate.vocabs import dc
from rdfcrate.wrapper import RoCrate


class RootDataEntity(sdo.Dataset):
    def __init__(
        self,
        name: sdo.name,
        description: sdo.description,
        date_published: sdo.datePublished,
        license: sdo.license,
        *args: EntityArgs,
        crate: RoCrate,
    ) -> None:
        return super().__init__(
            crate.root_data_entity.id, name, description, date_published, license, *args
        )


class MetadataEntity(sdo.CreativeWork):
    def __init__(self, *props: EntityArgs, crate: RoCrate) -> None:
        """
        Creates the `ro-crate-metadata.json` record.
        """
        return super().__init__(
            crate.metadata_entity.id,
            sdo.about(crate.root_data_entity),
            dc.conformsTo(dc.Standard(crate.version.conforms_to_url)),
            *props,
        )


class DataEntityMixin(sdo.CreativeWork):
    def link_to_dataset(
        self,
        dataset: sdo.Dataset,
    ) -> None:
        """
        Links a data entity to a Dataset.

        See https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/data-entities.html#referencing-files-and-folders-from-the-root-data-entity

        Params:
            entity: ID of the entity being linked
            dataset: ID of the dataset being linked to. If not provided, the entity will be linked to the root dataset.
        """
        dataset.props.append(sdo.hasPart(self))


class DirEntity(sdo.Dataset, DataEntityMixin):
    def __init__(
        self,
        path: str,
        *props: EntityArgs,
        crate: RoCrate,
        dataset: sdo.Dataset | None = None,
        **kwargs,
    ):
        """
        Adds metadata for a directory

        Returns:
            The ID of the new directory entity

        Params:
            path: Path to the directory, which must be within the crate root
            attrs: Attributes used to describe the `Dataset` entity
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.
            kwargs: Available for subclasses to extend the functionality.

        Example:
            ```python
            from rdfcrate import AttachedCrate
            from rdfcrate.vocabs import sdo as sdo

            AttachedCrate(".").register_dir("./some/dir", sdo.description(sdo.Text("This is a directory I am describing")))
            ```
        """
        if not path.endswith("/"):
            # Directories must end with a slash in RO-Crate
            path += "/"
        super().__init__(path, *props)
        if dataset is None:
            dataset = crate.root_data_entity
        if crate.root_data_entity.id != self.id:
            # The root dataset is not linked to itself
            self.link_to_dataset(dataset)


class FileEntity(roc.File, DataEntityMixin):
    def __init__(
        self,
        path: str,
        *args: EntityArgs,
        crate: RoCrate,
        guess_mime: bool = True,
        dataset: sdo.Dataset | None = None,
        **kwargs,
    ):
        """
        Adds file metadata to the crate

        Returns: The ID of the new file entity

        Params:
            path: Path or URL to the file being added
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.

        Example:
            ```python
            from rdfcrate import AttachedCrate
            from rdfcrate.vocabs import sdo as sdo

            AttachedCrate(".").register_file("./some/data.txt", sdo.description(sdo.Text("This is a file with some data")))
            ```
        """
        props = list(args)
        if guess_mime:
            if any(isinstance(arg, sdo.encodingFormat) for arg in args):
                raise ValueError(
                    "Cannot guess MIME type when encodingFormat is provided"
                )
            guess_type, _guess_encoding = mimetypes.guess_type(path)
            if guess_type is not None:
                props.append(sdo.encodingFormat(sdo.Text(guess_type)))
        super().__init__(path, *args, **kwargs)

        if dataset is None:
            dataset = crate.root_data_entity
        self.link_to_dataset(dataset)
