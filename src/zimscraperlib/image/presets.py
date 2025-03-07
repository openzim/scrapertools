from zimscraperlib.image.optimization import (
    OptimizeGifOptions,
    OptimizeJpgOptions,
    OptimizePngOptions,
    OptimizeWebpOptions,
)

""" presets for ImageOptimizer in zimscraperlib.image.optimization module """

preset_type = "image"


class WebpLow:
    """Low quality WebP image

    Lossy compression
    Low quality (Pillow quality is 40)
    Quality/Speed tradeoff is High"""

    VERSION = 1

    ext = "webp"
    mimetype = f"{preset_type}/webp"

    options: OptimizeWebpOptions = OptimizeWebpOptions(
        lossless=False,
        quality=40,
        method=6,
    )


class WebpMedium:
    """Medium quality WebP image

    Lossy compression
    High quality (Pillow quality is 65)
    Quality/Speed tradeoff is High"""

    VERSION = 1

    ext = "webp"
    mimetype = f"{preset_type}/webp"

    options: OptimizeWebpOptions = OptimizeWebpOptions(
        lossless=False,
        quality=50,
        method=6,
    )


class WebpHigh:
    """High quality WebP image

    Lossy compression
    High quality (Pillow quality is 60)
    Quality/Speed tradeoff is High"""

    VERSION = 1

    ext = "webp"
    mimetype = f"{preset_type}/webp"

    options: OptimizeWebpOptions = OptimizeWebpOptions(
        lossless=False,
        quality=90,
        method=6,
    )


class GifLow:
    """Low quality GIF image

    Strongest optimization level
    Colors limited to 256
    High Lossiness
    No extensions in GIF
    Interlaced frames"""

    VERSION = 1

    ext = "gif"
    mimetype = f"{preset_type}/gif"

    options: OptimizeGifOptions = OptimizeGifOptions(
        optimize_level=3,
        max_colors=256,
        lossiness=80,
        no_extensions=True,
        interlace=True,
    )


class GifMedium:
    """Medium quality GIF image

    Strong optimization level
    Colors not limited
    Low lossiness
    No extensions in GIF
    Interlaced frames"""

    VERSION = 1

    ext = "gif"
    mimetype = f"{preset_type}/gif"

    options: OptimizeGifOptions = OptimizeGifOptions(
        optimize_level=3,
        lossiness=20,
        no_extensions=True,
        interlace=True,
    )


class GifHigh:
    """High quality GIF image

    Weak optimization level
    Colors not limited
    Lossless compression
    No extensions in GIF
    Interlaced frames"""

    VERSION = 1

    ext = "gif"
    mimetype = f"{preset_type}/gif"

    options: OptimizeGifOptions = OptimizeGifOptions(
        optimize_level=2,
        lossiness=None,
        no_extensions=True,
        interlace=True,
    )


class PngLow:
    """Low quality PNG image

    Reduce colors to 256
    Slower and better compression"""

    VERSION = 1

    ext = "png"
    mimetype = f"{preset_type}/png"

    options: OptimizePngOptions = OptimizePngOptions(
        reduce_colors=True,
        remove_transparency=False,
        max_colors=256,
        fast_mode=False,
    )


class PngMedium:
    """Medium quality PNG image

    Reduce colors
    Slower and better compression"""

    VERSION = 1

    ext = "png"
    mimetype = f"{preset_type}/png"

    options: OptimizePngOptions = OptimizePngOptions(
        reduce_colors=False,
        remove_transparency=False,
        fast_mode=False,
    )


class PngHigh:
    """High quality PNG image

    Do not reduce colors
    Weaker and faster compression"""

    VERSION = 1

    ext = "png"
    mimetype = f"{preset_type}/png"

    options: OptimizePngOptions = OptimizePngOptions(
        reduce_colors=False,
        remove_transparency=False,
        fast_mode=True,
    )


class JpegLow:
    """Low quality JPEG image

    Low quality (40)
    Strip out exif data
    Slower and better compression"""

    VERSION = 1

    ext = "jpg"
    mimetype = f"{preset_type}/jpeg"

    options: OptimizeJpgOptions = OptimizeJpgOptions(
        quality=45,
        keep_exif=False,
        fast_mode=True,
    )


class JpegMedium:
    """Medium quality JPEG image

    Average quality (65)
    Strip out exif data
    Slower and better compression"""

    VERSION = 1

    ext = "jpg"
    mimetype = f"{preset_type}/jpeg"

    options: OptimizeJpgOptions = OptimizeJpgOptions(
        quality=65,
        keep_exif=False,
        fast_mode=True,
    )


class JpegHigh:
    """High quality JPEG image

    High quality (80)
    Do not strip out exif data
    Weaker and faster compression"""

    VERSION = 1

    ext = "jpg"
    mimetype = f"{preset_type}/jpeg"

    options: OptimizeJpgOptions = OptimizeJpgOptions(
        quality=80,
        keep_exif=True,
        fast_mode=True,
    )
