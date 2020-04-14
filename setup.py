from setuptools import setup
from setuptools import setup
from setuptools.command.develop import develop


class OldDevelopCommand(develop):
    def run(self):
        print("magic_hw")
        install.run(self)


class CustomDevelopCommand(OldDevelopCommand):

    def run(self):
        super().run(super())
        print("Hello, developer, how are you? :)")
        install.run(self)


######
setup(
    name="vegitelegram",
    version="0.0.1",
    author="BarBar",
    url='#',
    author_email='bb@bb.com',
    description=("For my favourite vegi store "),
    license='MIT',
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    zip_safe=False
)
