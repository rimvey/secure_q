<?php
$uploadDir = __DIR__ . "/uploads/";

if (isset($_FILES["attachment"])) {
    $file = $_FILES["attachment"];
    if ($file["error"] !== UPLOAD_ERR_OK) {
        http_response_code(400);
        exit("upload failed");
    }
    $target = $uploadDir . basename($file["name"]);
    if (move_uploaded_file($file["tmp_name"], $target)) {
        echo "uploaded: /uploads/" . basename($file["name"]);
    } else {
        http_response_code(500);
        echo "save failed";
    }
}
?>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="attachment">
  <button type="submit">전송</button>
</form>
