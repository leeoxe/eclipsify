projectTemplate=R'''<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
	<name>aslam_cv</name>
	<comment></comment>
	<projects>
	</projects>
	<buildSpec>
		<buildCommand>
			<name>org.eclipse.cdt.managedbuilder.core.genmakebuilder</name>
			<triggers>clean,full,incremental,</triggers>
			<arguments>
			</arguments>
		</buildCommand>
		<buildCommand>
			<name>org.eclipse.cdt.managedbuilder.core.ScannerConfigBuilder</name>
			<triggers>full,incremental,</triggers>
			<arguments>
			</arguments>
		</buildCommand>
	</buildSpec>
	<natures>
		<nature>org.eclipse.cdt.core.cnature</nature>
		<nature>org.eclipse.cdt.core.ccnature</nature>
		<nature>org.eclipse.cdt.managedbuilder.core.managedBuildNature</nature>
		<nature>org.eclipse.cdt.managedbuilder.core.ScannerConfigNature</nature>
	</natures>
	<linkedResources>
		<link>
			<name>{0}_src</name>
			<type>2</type>
			<location>{1}</location>
		</link>
	</linkedResources>
</projectDescription>
'''

def get(packageName, fullPathToSource):
    return projectTemplate.format(packageName, fullPathToSource)