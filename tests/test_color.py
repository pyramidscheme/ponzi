from typing import NamedTuple

from pytest import approx

from ponzi.color.space import (
    RGB,
    Lab,
    HCL,
    XYZ,
    LinearRGB,
    hcl_to_lab,
    lab_to_hcl,
    lab_to_xyz,
    xyz_to_lab,
    xyz_to_linear_rgb,
    linear_rgb_to_xyz,
    srgb_to_linear_rgb,
    linear_rgb_to_srgb,
)
from ponzi.color.linear import delinearize, linearize


class Case(NamedTuple):
    hex: str
    rgb: RGB
    lrgb: LinearRGB
    xyz: XYZ
    lab: Lab
    hcl: HCL


cases = [
    Case(
        "#ffffff",
        RGB(1.0, 1.0, 1.0),
        LinearRGB(1, 1, 1),
        XYZ(0.950470, 1.000000, 1.088830),
        Lab(1.000000, 0.000000, 0.000000),
        HCL(0.0000, 0.000000, 1.000000),
    ),
    Case(
        "#80ffff",
        RGB(0.5, 1.0, 1.0),
        LinearRGB(0.21404114048223255, 1, 1),
        XYZ(0.626296, 0.832848, 1.073634),
        Lab(0.931390, -0.353319, -0.108946),
        HCL(197.1371, 0.369735, 0.931390),
    ),
    Case(
        "#ff80ff",
        RGB(1.0, 0.5, 1.0),
        LinearRGB(1, 0.21404114048223255, 1),
        XYZ(0.669430, 0.437920, 0.995150),
        Lab(0.720892, 0.651673, -0.422133),
        HCL(327.0661, 0.776450, 0.720892),
    ),
    Case(
        "#ffff80",
        RGB(1.0, 1.0, 0.5),
        LinearRGB(1, 1, 0.21404114048223255),
        XYZ(0.808654, 0.943273, 0.341930),
        Lab(0.977637, -0.165795, 0.602017),
        HCL(105.3975, 0.624430, 0.977637),
    ),
    Case(
        "#8080ff",
        RGB(0.5, 0.5, 1.0),
        LinearRGB(0.21404114048223255, 0.21404114048223255, 1),
        XYZ(0.345256, 0.270768, 0.979954),
        Lab(0.590453, 0.332846, -0.637099),
        HCL(297.5843, 0.718805, 0.590453),
    ),
    Case(
        "#ff8080",
        RGB(1.0, 0.5, 0.5),
        LinearRGB(1, 0.21404114048223255, 0.21404114048223255),
        XYZ(0.527613, 0.381193, 0.248250),
        Lab(0.681085, 0.483884, 0.228328),
        HCL(25.2610, 0.535049, 0.681085),
    ),
    Case(
        "#80ff80",
        RGB(0.5, 1.0, 0.5),
        LinearRGB(0.21404114048223255, 1, 0.21404114048223255),
        XYZ(0.484480, 0.776121, 0.326734),
        Lab(0.906026, -0.600870, 0.498993),
        HCL(140.2920, 0.781050, 0.906026),
    ),
    Case(
        "#808080",
        RGB(0.5, 0.5, 0.5),
        LinearRGB(0.21404114048223255, 0.21404114048223255, 0.21404114048223255),
        XYZ(0.203440, 0.214041, 0.233054),
        Lab(0.533890, 0.000000, 0.000000),
        HCL(0.0000, 0.000000, 0.533890),
    ),
    Case(
        "#00ffff",
        RGB(0.0, 1.0, 1.0),
        LinearRGB(0.0, 1.0, 1.0),
        XYZ(0.538014, 0.787327, 1.069496),
        Lab(0.911132, -0.480875, -0.141312),
        HCL(196.3762, 0.501209, 0.911132),
    ),
    Case(
        "#ff00ff",
        RGB(1.0, 0.0, 1.0),
        LinearRGB(1.0, 0.0, 1.0),
        XYZ(0.592894, 0.284848, 0.969638),
        Lab(0.603242, 0.982343, -0.608249),
        HCL(328.2350, 1.155407, 0.603242),
    ),
    Case(
        "#ffff00",
        RGB(1.0, 1.0, 0.0),
        LinearRGB(1.0, 1.0, 0.0),
        XYZ(0.770033, 0.927825, 0.138526),
        Lab(0.971393, -0.215537, 0.944780),
        HCL(102.8512, 0.969054, 0.971393),
    ),
    Case(
        "#0000ff",
        RGB(0.0, 0.0, 1.0),
        LinearRGB(0.0, 0.0, 1.0),
        XYZ(0.180437, 0.072175, 0.950304),
        Lab(0.322970, 0.791875, -1.078602),
        HCL(306.2849, 1.338076, 0.322970),
    ),
    Case(
        "#00ff00",
        RGB(0.0, 1.0, 0.0),
        LinearRGB(0.0, 1.0, 0.0),
        XYZ(0.357576, 0.715152, 0.119192),
        Lab(0.877347, -0.861827, 0.831793),
        HCL(136.0160, 1.197759, 0.877347),
    ),
    Case(
        "#ff0000",
        RGB(1.0, 0.0, 0.0),
        LinearRGB(1.0, 0.0, 0.0),
        XYZ(0.412456, 0.212673, 0.019334),
        Lab(0.532408, 0.800925, 0.672032),
        HCL(39.9990, 1.045518, 0.532408),
    ),
    Case(
        "#000000",
        RGB(0.0, 0.0, 0.0),
        LinearRGB(0.0, 0.0, 0.0),
        XYZ(0.000000, 0.000000, 0.000000),
        Lab(0.000000, 0.000000, 0.000000),
        HCL(0.0000, 0.000000, 0.000000),
    ),
]


def test_linear_rgb():
    for c in cases:
        actual = srgb_to_linear_rgb(c.rgb)
        assert actual.r == approx(c.lrgb.r, 0.0001)
        assert actual.g == approx(c.lrgb.g, 0.0001)
        assert actual.b == approx(c.lrgb.b, 0.0001)
    for c in cases:
        actual = linear_rgb_to_srgb(c.lrgb)
        assert actual.r == approx(c.rgb.r, 0.0001)
        assert actual.g == approx(c.rgb.g, 0.0001)
        assert actual.b == approx(c.rgb.b, 0.0001)


def test_xyz():
    for c in cases:
        actual = linear_rgb_to_xyz(srgb_to_linear_rgb(c.rgb))
        assert actual.x == approx(c.xyz.x, 0.0001)
        assert actual.y == approx(c.xyz.y, 0.0001)
        assert actual.z == approx(c.xyz.z, 0.0001)
    for c in cases:
        actual = linear_rgb_to_srgb(xyz_to_linear_rgb(c.xyz))
        assert actual.r == approx(c.rgb.r, 0.0001, 0.0001)
        assert actual.g == approx(c.rgb.g, 0.0001, 0.0001)
        assert actual.b == approx(c.rgb.b, 0.0001, 0.0001)


def test_lab():
    for c in cases:
        actual = xyz_to_lab(linear_rgb_to_xyz(srgb_to_linear_rgb(c.rgb)))
        assert actual.l == approx(c.lab.l, 0.0001, 0.0001)
        assert actual.a == approx(c.lab.a, 0.0001, 0.0001)
        assert actual.b == approx(c.lab.b, 0.0001, 0.0001)
    for c in cases:
        actual = linear_rgb_to_srgb(xyz_to_linear_rgb(lab_to_xyz(c.lab)))
        assert actual.r == approx(c.rgb.r, 0.0001, 0.0001)
        assert actual.g == approx(c.rgb.g, 0.0001, 0.0001)
        assert actual.b == approx(c.rgb.b, 0.0001, 0.0001)


def test_hcl():
    for c in cases:
        actual = lab_to_hcl(xyz_to_lab(linear_rgb_to_xyz(srgb_to_linear_rgb(c.rgb))))
        assert actual.h == approx(c.hcl.h, 0.0001, 0.0001)
        assert actual.c == approx(c.hcl.c, 0.0001, 0.0001)
        assert actual.l == approx(c.hcl.l, 0.0001, 0.0001)
    for c in cases:
        actual = linear_rgb_to_srgb(xyz_to_linear_rgb(lab_to_xyz(hcl_to_lab(c.hcl))))
        assert actual.r == approx(c.rgb.r, 0.0001, 0.0001)
        assert actual.g == approx(c.rgb.g, 0.0001, 0.0001)
        assert actual.b == approx(c.rgb.b, 0.0001, 0.0001)


def test_linearize():
    assert linearize(0.000000) == approx(0.000000)
    assert linearize(0.040000) == approx(0.003096, 0.0001)
    assert linearize(0.100000) == approx(0.010023, 0.0001)
    assert linearize(0.200000) == approx(0.033105, 0.0001)
    assert linearize(0.250000) == approx(0.050876, 0.0001)
    assert linearize(0.500000) == approx(0.214041, 0.0001)
    assert linearize(0.750000) == approx(0.522522, 0.0001)
    assert linearize(1.000000) == approx(1.000000, 0.0001)


def test_delinearize():
    assert delinearize(0.000000) == approx(0.000000, 0.0001, 0.0001)
    assert delinearize(0.003000) == approx(0.038760, 0.0001, 0.0001)
    assert delinearize(0.010000) == approx(0.099853, 0.0001, 0.0001)
    assert delinearize(0.050000) == approx(0.247801, 0.0001, 0.0001)
    assert delinearize(0.100000) == approx(0.349190, 0.0001, 0.0001)
    assert delinearize(0.200000) == approx(0.484529, 0.0001, 0.0001)
    assert delinearize(0.250000) == approx(0.537099, 0.0001, 0.0001)
    assert delinearize(0.500000) == approx(0.735357, 0.0001, 0.0001)
    assert delinearize(0.750000) == approx(0.880825, 0.0001, 0.0001)
    assert delinearize(1.000000) == approx(1.000000, 0.0001, 0.0001)
