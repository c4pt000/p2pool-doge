<?php
	// Recommended to force host, otherwise anyone can shoot out web requests on your servers behalf.
	$force_host = false;
	$force_host_address = "http://p2pool.org:9332";

	if (!isset($_GET['report']) || !isset($_GET['host']))
	{
		die("Invalid Request.");
	}

	$report = $_GET['report']; 
	$host = $_GET['host'];
	$web_url = $host . $report;

	// Make sure the file isn't a local file, otherwise an attacker could fetch any file off your server.
	if (file_exists($web_url))
	{
		die("Access Denied.");
	}

	// Parse the URL to make sure its valid.
	if (!filter_var($web_url, FILTER_VALIDATE_URL))
	{
		die("Invalid Host.");
	}

	// Check if the host is whitelisted.
	if ($force_host && $host != $force_host_address)
	{
		die("Invalid Host.");
	}
	
	$json = file_get_contents($web_url);
	echo sprintf('%s(%s);', $_GET['callback'], $json);  
?>
