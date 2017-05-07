#These and other macros are documented in dhd/droid-hal-device.inc
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}
%define device eva
%define vendor huawei
%define vendor_pretty Huawei
%define device_pretty P9
%define installable_zip 1
%include rpm/dhd/droid-hal-device.inc
