<!DOCTYPE html>
<html lang="de">
<html>
    <head>
    <meta charset="utf-8">
    <style>
      table{border:1 px solid black;}

      </style>
      </head>
      <body>
        <html lang ="de">
        <head>
        <link rel="stylesheet" href="style.css"/>
        <meta name="viewport" content="width=device-width,initialscale=1.0"/>

        <title> Aufgabe 1</title>
        </head>
      </body>
          <h1>Übungsaufgabe 2 -Werteliste</h1>
<?php
$miniw = $_POST["miniw"];
$maxiw = $_POST["maxiw"];
if(empty($miniw) || empty($maxiw)) {
  echo "Bitte füllen Sie beide Felder aus!";
}
elseif ($miniw <= 0) {
  echo 'Der minimaler Winkel muss positiv sein!';
}

elseif($maxiw > 360) {
  ?>
  <?php echo '<p> Der maximaler Winkel muss kleiner als 360° sein!</p>' ?>
  <?php
}
elseif($miniw >= $maxiw){
    ?>
    <div>
    <style>
      div
      {
        background-color: yellow;
        border: 1px solid;
        border-color: red;
        padding : 2px;
        font-weight: bold;
      }
    </style>
    <?php echo '<p>Der minimale Winkel muss kleiner als der maximale Winkel sein!</p>' ?>
  </div>
    <?php
  }
  else{
    ?>
    <style>
     table, th, td
     {
       border : 1px solid black;
       border-collapse: collapse;
     }
   </style>
   <table style="width:100%">
  <tr><td>Winkel in °</td><td>Sin</td><td>Cos</td><td>Tan</td>
   <?php for ($i = $maxiw -($maxiw - $miniw); $i <= $maxiw; $i++){
     echo '<tr><td>'.$i.'</td><td>'.sin(deg2rad($i)).'</td><td>'.cos(deg2rad($i)).'</td><td>'.tan(deg2rad($i)).'</td></tr>';
     }
   } ?>
  </tr>
   </table>


     <p> Aktuelle Serverzeit:

       <?php
       $datum = date("d.m.Y");
       $uhrzeit = date("H:i:s");
       echo $uhrzeit , "Uhr am",$datum;
       ?>
     </p>

  </html>
