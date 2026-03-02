# Créative & Technologique

```{toctree}
:maxdepth: 2
:hidden:

1-Obj-src/crea-v-obj-src
2-Stockage/crea-v-stock
3-Traitement/crea-v-analyse
4-Partage/crea-v-partage

```



## Test

```{note}

Import tableau Frama

```

<iframe 
    src="https://4-a.frama.space/apps/tables/api/1/views/2"
    width="100%" 
    height="600"
    frameborder="0">
</iframe>


<div id="frama-data"></div>

<script>
    fetch("https://4-a.frama.space/apps/tables/api/1/views/2")
      .then(response => response.json())
      .then(data => {
          let html = "<ul>";
          data.results.forEach(item => {
              html += "<li>" + item.Nom + "</li>";
          });
          html += "</ul>";
          document.getElementById("frama-data").innerHTML = html;
      })
      .catch(error => {
          document.getElementById("frama-data").innerHTML = "Erreur de chargement";
      });
</script>