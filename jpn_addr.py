import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
)


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "jpn_addr"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text/addr"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(30, 31),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)

training_cities_data = GeneratorCfg(
    num_image=50000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "cities.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

training_areas_data = GeneratorCfg(
    num_image=100000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "areas.txt"],
                filter_by_chars=True,
                length=(10, 20),
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

training_numbers_data = GeneratorCfg(
    num_image=100000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "numbers.txt"],
                filter_by_chars=True,
                length=(10, 20),
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

training_details_data = GeneratorCfg(
    num_image=300000,
    save_dir=OUT_DIR / "training",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "details.txt"],
                filter_by_chars=True,
                length=(10, 20),
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_cities_data = GeneratorCfg(
    num_image=5000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "cities.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_areas_data = GeneratorCfg(
    num_image=10000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "areas.txt"],
                filter_by_chars=True,
                length=(10, 20),
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_numbers_data = GeneratorCfg(
    num_image=10000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "numbers.txt"],
                filter_by_chars=True,
                length=(10, 20),
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)

evaluation_details_data = GeneratorCfg(
    num_image=30000,
    save_dir=OUT_DIR / "evaluation",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "details.txt"],
                filter_by_chars=True,
                length=(10, 20),
                chars_file=CHAR_DIR / "chars.txt",
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
    ),
)


# fmt: off
configs = [
    training_cities_data,
    training_areas_data,
    training_numbers_data,
    training_details_data,
    evaluation_cities_data,
    evaluation_areas_data,
    evaluation_numbers_data,
    evaluation_details_data,
]
# fmt: on
