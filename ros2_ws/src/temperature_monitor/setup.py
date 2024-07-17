from setuptools import find_packages, setup

package_name = 'temperature_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rony',
    maintainer_email='rony.kaddoum.2013@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_meter_node = temperature_monitor.temperature_meter:main',
            'threshold_alerter_node = temperature_monitor.threshold_alerter:main',
            'alert_publisher_node = temperature_monitor.alert_publisher:main',
        ],
    },
)
