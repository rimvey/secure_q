<?php
$result = "";

if (isset($_GET["host"])) {
    $host = $_GET["host"];
    $output = shell_exec("ping -c 2 " . $host);
    $result = htmlspecialchars($output ?? "", ENT_QUOTES, "UTF-8");
}
?>
<html>
<body>
<h1>서버 상태 확인</h1>
<form method="get">
  <input type="text" name="host" placeholder="호스트 이름">
  <button type="submit">확인</button>
</form>
<pre><?php echo $result; ?></pre>
</body>
</html>
