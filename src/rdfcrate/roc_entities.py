import mimetypes
from rdfcrate import sdo, roc
from rdfcrate.context_graph import EntityArgs
from rdfcrate.vocabs import dc
from rdfcrate.wrapper import RoCrate


class RootDataEntity(sdo.Dataset):
    """
    The root data entity "./" for the crate.
    """

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
    """
    The `ro-crate-metadata.json` record.
    """
    def __init__(self, *props: EntityArgs, crate: RoCrate) -> None:
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
    """
    Represents an RO-Crate directory entity.
    """

    def __init__(
        self,
        path: str,
        *props: EntityArgs,
        **kwargs,
    ):
        """
        Params:
            path: Path to the directory, which must be within the crate root
            props: Attributes used to describe the `Dataset` entity
            kwargs: Available for subclasses to extend the functionality.
        """
        if not path.endswith("/"):
            # Directories must end with a slash in RO-Crate
            path += "/"
        super().__init__(path, *props)


class FileEntity(roc.File, DataEntityMixin):
    """
    An RO-Crate file entity.
    """

    def __init__(
        self,
        path: str,
        *args: EntityArgs,
        guess_mime: bool = True,
        **kwargs,
    ):
        """
        Params:
            path: Path or URL to the file being added
            args: Additional properties to add to the file entity
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension
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
