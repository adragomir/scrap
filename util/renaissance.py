import objc, AppKit, Foundation, os
base_path = '/Library/Frameworks'
bundle_path = os.path.abspath(os.path.join(base_path, 'Renaissance.framework'))
print bundle_path
objc.loadBundle('Renaissance', globals(), bundle_path=bundle_path)
del objc, AppKit, Foundation, os, base_path, bundle_path
