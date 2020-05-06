<template>
  <div class="event-single">
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            {{ event.name }}
          </h1>
          <h2 class="subtitle ">
            <strong>Date:</strong> {{ event.date }}
            <br>
            <strong>Time:</strong> {{ event.time }}
          </h2>
        </div>
      </div>
    </section>
    <section class="event-content">
      <div class="container">
        <p class="is-size-4 description">{{ event.description }}</p>
        <p class="is-size-5"><strong>Location:</strong> {{ event.location }}</p>
        <p class="is-size-5"><strong>Category:</strong> {{ event.category }}</p>
        <div class="event-images columns is-multiline has-text-centered">
          <div v-for="image in event.images" :key="image.id" class="column is-one-third">
            <img :src="image" :alt="event.name">
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// NEW - import EventService
import EventService from '@/services/EventService.js';

export default {
  name: 'EventSingle',

  data() {
    // NEW - initialize the event object
    return {
      event: {}
    }
  },

  created() {
    this.getEventData(); // NEW - call getEventData() when the instance is created
  },

  // NEW
  methods: {

    async getEventData() {

      // Get the access token from the auth wrapper
      const accessToken = await this.$auth.getTokenSilently();

      // Use the eventService to call the getEventSingle() method
      EventService.getEventSingle(this.$route.params.id, accessToken)
      .then(
        (event => {
          // this.$set is an alias for 'Vue.set'. The second 'this'
          // is again referencing the Vue instance, the first "event"
          // represents the property we are setting and assign the
          // event object we received from the API. Have a look at
          // the subject Reactivity in Vue: https://vuejs.org/v2/guide/reactivity.html
          this.$set(this, "event", event);
          console.log(this);
        }).bind(this)
      );
    }

  }

}
</script>