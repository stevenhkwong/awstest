<?php

	$keyid = "";
	$secret = "";
	$instance = "";
	$qty = "";
	$status_msg = "";
	$status_array = [];

	foreach ( $_POST as $key => $value ) {
		if ( $key == 'key' ) {
			$keyid=$value;
		}
		if ( $key == 'secret' ) {
			$secret=$value;
		}
		if ( $key == 'qty' ) {
			$qty=$value;
		}
		if ( $key == 'instance' ) {
			$instance=$value;
		}
	}
	if(isset($_POST["launch"])) {
		$launch_status = shell_exec ('./i_start.py -q ' . $qty . ' -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$status_msg = $launch_status . shell_exec ('./i_status.py -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$status_array = split ("\n", $status_msg);
		$ids = shell_exec ('./i_status.py -r -l -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$ids_array = split ("\n", $ids);
	}
	if(isset($_POST["terminate"])) {
		$terminate_status = shell_exec ('./i_destroy.py -i ' . $instance . ' -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$status_msg = $terminate_status . shell_exec ('./i_status.py -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$status_array = split ("\n", $status_msg);
		$ids = shell_exec ('./i_status.py -r -l -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$ids_array = split ("\n", $ids);
	}
	if(isset($_POST["status"])) {
		$status_msg = shell_exec ('./i_status.py -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$status_array = split ("\n", $status_msg);
		$ids = shell_exec ('./i_status.py -r -l -k ' . $keyid . ' -s ' . $secret . ' 2>&1');
		$ids_array = split ("\n", $ids);
	}

?>
<form style="border: black solid 1px" autocomplete="off" action="<?= $_SERVER['PHP_SELF'] ?>" method="post" name="launch">
<p><label style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >key:</label><input name="key" ></input></p>
<p><label for="secret" style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >secret:</label><input name="secret" type="password" ></input></p>
<p><label for="ip" style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >Number of instances to launch:</label><input name="qty" type="text" /></p>
<p><input type="submit" name="launch" value="Launch" /></p>
</form>

<form style="border: black solid 1px" autocomplete="off" action="<?= $_SERVER['PHP_SELF'] ?>" method="post" name="terminate">
<p><label style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >key:</label><input name="key" ></input></p>
<p><label for="secret" style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >secret:</label><input name="secret" type="password" ></input></p>
<p><label style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >Instance:</label><select id=instance name=instance value="U" >
<?php
	foreach ($ids_array as $id) {
		echo '<option value=' . $id . '>' . $id . '</option>';
	}
?>
</select></p>
<p><input type="submit" name="terminate" value="Terminate" /></p>

</form>

<form style="border: black solid 1px" autocomplete="off" action="<?= $_SERVER['PHP_SELF'] ?>" method="POST" name="terminate">
<p><label style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >key:</label><input name="key" ></input></p>
<p><label for="secret" style="float: left; width: 200px; margin-right: 10px; text-align: right; font-weight: bold; clear: left;" >secret:</label><input name="secret" type="password" ></input></p>
<p><input type="submit" name="status" value="status" /></p>

<div style="border: black double 1px" >
        <label>Status:</label>
				<?php
					foreach ( $status_array as $line ) {
						echo $line . "<br>";
					}
				?>
</div>

