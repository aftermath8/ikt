<meta charset="UTF-8">
<html>
 <head>
  <title>PHP-Test</title>
 </head>
 <body>
   <form action="u2_werteliste.php" method="post">

 <header>
   <style>
   header
   {
     color: black;
     background: lightblue;
     padding : 10px;
   }
   </style>
 <?php echo '<h1> Übungsaufgabe 2 - Eingabe des Winkelbereichs</h1>'; ?>
</header>

<br/>

<div>
  <label for="miniw">Minimaler Winkel</label>
  <br/>
  <input type="number" step="any" name="miniw">
  <br/><br />
  <label for="maxiw">Maximaler Winkel</label>
  <br/>
  <input type="number" step="any" name="maxiw">
</div>
</br>
<input type="submit" value="Berechnen">
</br>
</br>
<footer>
  <style>
  footer
  {
    background: lightblue;
  }
  </style>

<?php
$datum = date("d.m.Y");
$hour = date("H:i:s");
echo "Aktueller Serverzeit ist: $hour am $datum";
?>

</footer>
</form>
</body>
</html>
