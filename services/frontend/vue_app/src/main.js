import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './../node_modules/bulma/css/bulma.css';

/** Import the Auth0 configuration */
import {AUTH0_CONF} from "@/config/config.js";

const domain = AUTH0_CONF.domain
const clientId = AUTH0_CONF.clientId
const audience = AUTH0_CONF.audience

/** Import the Auth0Plugin we created in the /auth/index.js at the end of the file
 * to use it throughout the whole application */
import {Auth0Plugin} from "@/auth";

/** Install the authentication plugin here */
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
