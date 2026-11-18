<?php
session_start();

$comments = [];
$db = new PDO("sqlite:board.db");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $stmt = $db->prepare("INSERT INTO comments (author, body) VALUES (?, ?)");
    $stmt->execute([$_POST["author"], $_POST["body"]]);
}

foreach ($db->query("SELECT author, body FROM comments ORDER BY id DESC") as $row) {
    $comments[] = $row;
}
?>
<html>
<body>
<h1>방명록</h1>
<?php foreach ($comments as $c): ?>
  <div class="comment">
    <strong><?php echo $c["author"]; ?></strong>
    <p><?php echo $c["body"]; ?></p>
  </div>
<?php endforeach; ?>
</body>
</html>
