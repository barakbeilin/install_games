from setuptools import setup
from setuptools import setup
from setuptools.command.develop import develop


class OldDevelopCommand(develop):
    def run(self):
        print("SNAKE")
        develop.run(self)


class CustomDevelopCommand(OldDevelopCommand):

    def run(self):
        super().run()
        print("Hello, developer, how are you? :)")
        develop.run(self)


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
    zip_safe=False,
    cmdclass={
        'develop': CustomDevelopCommand,
    },
)
