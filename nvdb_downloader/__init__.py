def classFactory(iface):
    from .plugin import NvdbDownloaderPlugin

    return NvdbDownloaderPlugin(iface)
