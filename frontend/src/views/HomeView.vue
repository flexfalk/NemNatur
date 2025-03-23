<script setup>
import { ref, onMounted } from 'vue';

const produkter = ref([]);

onMounted(async () => {
  const response = await fetch('http://127.0.0.1:8000/products');
  produkter.value = await response.json();
});
</script>

<template>
  <div>
    <h1>Velkommen til NemNatur</h1>
    <p>Oplev sjove og lærerige naturoplevelser for børn og unge!</p>

    <!-- Image Banner Section -->
    <div class="image-banner">
      <img src="/hulebyg.jpg" alt="Smuk natur" />
    </div>

    <!-- Introduction Section -->
    <section class="intro">
      <h2>Vores Idé</h2>
      <p>NemNatur er skabt for at give børn og unge fantastiske naturoplevelser sammen med deres klassekammerater og stuekammerater. Vi ønsker at gøre det nemt for skoler og børnehaver at komme ud i naturen og opleve noget sjovt og lærerigt – alt sammen med fokus på leg, nysgerrighed og læring.</p>
    </section>

    <!-- Activities Section -->
    <section class="activities">
      <h2>Vore Aktiviteter</h2>
      <p>Vi tilbyder en bred vifte af aktiviteter, der engagerer børnene i naturen. Nogle af vores populære aktiviteter inkluderer:</p>
      <ul>
        <li>Bygge huler i skoven</li>
        <li>Lave bål med gammeldags tindjern</li>
        <li>Lege og udforske naturen</li>
        <li>Gå på svampejagt</li>
        <li>Undersøge insekter og dyr</li>
      </ul>
    </section>

    <!-- Call to Action Section -->
    <section class="cta">
      <h2>Book en tur i dag!</h2>
      <p>Kontakt os for at booke en uforglemmelig naturoplevelse for din skole eller børnehave.</p>
    </section>
  </div>
</template>

<style scoped>
.image-banner img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
}

/* Section Styles */
.intro, .activities, .products, .cta {
  padding: 40px;
  background-color: #fff;
  margin: 20px 0;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.intro h2, .activities h2, .products h2, .cta h2 {
  font-size: 2rem;
  color: #333;
}

.intro p, .activities p {
  font-size: 1.2rem;
  color: #555;
}

ul {
  list-style-type: disc;
  margin-left: 20px;
}

ul li {
  font-size: 1.1rem;
  margin: 5px 0;
}

.cta h2 {
  text-align: center;
}
</style>
