# These and other macros are documented in dhd/droid-hal-device.inc
%define device nozomi
%define vendor sony
%define vendor_pretty Sony
%define device_pretty Xperia S
%define installable_zip 1
%define straggler_files \
/init.qcom.class_core.sh \
/init.qcom.class_main.sh \
/init.qcom.sh \
/init.sh \
/init.swap.sh \
/init.usbmode.sh \
/logo.rle \
/selinux_version \
/service_contexts \
%{nil}
%include rpm/dhd/droid-hal-device.inc
