from setuptools import setup

setup(name='captionbot',
      version='0.1.4',
      description='Simple API wrapper for https://www.captionbot.ai/',
      url='http://github.com/krikunts/captionbot',
      author='Tatiana Krikun',
      author_email='krikunts@gmail.com',
      license='MIT',
      packages=['captionbot'],
      install_requires=[
        'requests',
      ],
      zip_safe=False)