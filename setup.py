from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup_info = dict(
    name='wandbviz',
    version='0.0.1',
    author='Aspiring Astro (@aspiringastro)',
    author_email='aspiringastro@gmail.com',
    url='https://github.com/aspiringastro/wandbviz',
    description='Weights and Bias visualizer that generates animated GIFs of training neural nets',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    license='MIT',
    install_requires=[ 'tqdm', 'torch', 'numpy', 'matplotlib', 'gif'],
    keywords='pytorch weights biases neural networks visualizaer bertviz',
    packages=["wandbviz"],
)

setup(**setup_info)