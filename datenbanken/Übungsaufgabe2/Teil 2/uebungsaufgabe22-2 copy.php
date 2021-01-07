<meta charset="UTF-8">
<html>
 <head>
  <title>PHP-Test</title>
 </head>
 <header>
   <style>
   header
   {
     color: black;
     background: lightblue;
     padding : 10px;
   }
   </style>
 <?php echo '<h1> Übungsaufgabe 2</h1>'; ?>
</header>

<br/>

<footer>
  <style>
  footer
  {
    background: lightblue;
  }
  </style>

<?php
$datum = date("d.m.Y H:i:s");
echo "Aktueller Serverzeit ist : $datum";
?>
</footer>
</html>
