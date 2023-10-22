from setuptools import find_packages, setup


def read_requirements(path: str) -> list:
    with open(path, "r") as fh:
        return fh.read().splitlines()


base_requirements = read_requirements("requirements.txt")


setup(
    name="speech-to-text",
    version="0.0.1",
    packages=find_packages(include=["speech_to_text.*"]),
    python_requires=">=3.9",
    install_requires=base_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text to speech recognition",
    ],
)
