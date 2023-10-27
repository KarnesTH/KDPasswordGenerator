#!/bin/sh
# Create folders
[ -e package ] && rm -r package
mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps

# Copy files
cp -r dist/kd-password-generator package/opt/kd-password-generator
cp img/logo.svg package/usr/share/icons/hicolor/scalable/apps/logo.svg
cp kd-password-generator.desktop package/usr/share/applications

# Change permissions
find package/opt/kd-password-generator -type f -exec chmod 644 -- {} +
find package/opt/kd-password-generator -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/kd-password-generator/kd-password-generator