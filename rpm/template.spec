Name:           ros-hydro-rosh-visualization
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS rosh_visualization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosh_visualization
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-image-view
Requires:       ros-hydro-rosh
Requires:       ros-hydro-roslib
BuildRequires:  ros-hydro-catkin

%description
ROSH plugin for the visualization stack.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Aug 22 2014 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.4-0
- Autogenerated by Bloom

* Sun Aug 17 2014 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.3-0
- Autogenerated by Bloom

