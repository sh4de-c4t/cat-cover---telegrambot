import setuptools


setuptools.setup(

    name="forwardscoverbot",
    version="1",

    license="AGPL-3.0",

    author="Dario 91DarioDev",
    author_email="dariomsn@hotmail.it",

    install_requires=[
        "python-telegram-bot",
        "Pyyaml"
    ],

    packages=[
        "forwardscoverbot",
    ],

    entry_points={
        "console_scripts": [
            "forwardscoverbot = forwardscoverbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
