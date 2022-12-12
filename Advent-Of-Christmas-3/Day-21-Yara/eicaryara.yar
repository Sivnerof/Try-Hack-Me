rule eicaryara {
	meta:
		author="tryhackme"
		description="eicar string"
	strings:
		$a="X5O"
		$b="EICAR"
		$c="ANTIVIRUS"
		$d="TEST"
	condition:
		$a and $b and $c and $d
}
