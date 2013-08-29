from pipeline.storage import PipelineCachedStorage


class PipelineForgivingStorage(PipelineCachedStorage):
    def hashed_name(self, name, content=None):
        try:
            out = super(PipelineForgivingStorage, self).hashed_name(name, content)
        except ValueError:
            # This means that a file could not be found, and normally this would
            # cause a fatal error, which seems rather excessive given that
            # some packages have missing files in their css all the time.
            out = name
        return out
