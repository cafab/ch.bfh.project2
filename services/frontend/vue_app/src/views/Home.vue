<template>
  <div class="home">
    <section class="hero is-link">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Welcome to the BFH Project 2</h1>
          <h3 v-if="$auth.isAuthenticated" class="is-size-3 welcome">
            Welcome, {{ $auth.user.name }}!
          </h3>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

export default {
  name: 'home'
}

</script>

<style lang="scss" scoped>
.hero {
  text-align: center;
  background-color: #222b58fb;
  height: 400px;
}
.hero-body .title {
  text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.6);
  padding: 40px 0 20px 0;
  font-size: 60px;
}
.subtitle {
  text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.7);
  font-size: 30px;
}
.button-block {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  position: absolute;
  bottom: -150px;
  .button {
    margin-right: 50px;
    padding-left: 50px;
    padding-right: 50px;
  }
  .welcome {
    width: 400px;
    padding: 10px;
    margin-left: auto;
    margin-right: auto;
  }
}
.is-xl {
  font-size: 1.7rem;
}
</style>
