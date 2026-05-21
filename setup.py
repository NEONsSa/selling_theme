from setuptools import setup, find_packages

setup(
    name="selling_theme",
    version="0.0.1",
    description="Bold & Colorful Light Mode theme for ERPNext Selling module",
    author="NEONS",
    author_email="admin@bpo.sa",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
