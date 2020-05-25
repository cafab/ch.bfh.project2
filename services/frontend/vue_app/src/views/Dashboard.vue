<template>
  <div class="about">
    <div class="hero is-link">
      <div class="hero-body">
        <div class="container">
          <h1 class="title is-size-1">Dashboard</h1>        
        </div>
      </div>
    </div>
    <div class="container">
      <p class="org-description is-size-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius quia aperiam eligendi dolorum reprehenderit ea amet, aliquid dolorem beatae, iste aliquam ullam. Sequi ab eligendi consectetur neque laudantium, libero asperiores.</p>
      <p class="org-description is-size-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius quia aperiam eligendi dolorum reprehenderit ea amet, aliquid dolorem beatae, iste aliquam ullam. Sequi ab eligendi consectetur neque laudantium, libero asperiores.</p>
    </div>
  </div>
</template>

<script>

import UserService from '@/services/UserService.js'

export default {

  name: 'dashboard',

  data() {
    return {
      activeBot: false
    }
  },

  created() {
    this.registerUser()
  },

  methods: {

    async registerUser() {
      
      const accessToken = await this.$auth.getTokenSilently()
      const email = await this.$auth.user.email

      UserService.registerUser(accessToken, email)
      .then(
        res => console.log(res)
      );

    }
  }
}

</script>

<style lang="scss" scoped>
  .org-description {
    margin-top: 50px;
  }
</style>