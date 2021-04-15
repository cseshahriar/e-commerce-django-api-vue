<template>
  <div class="wrapper">
    
    <!-- navbar -->
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
        </a>

        <a role="button" class="navbar-burger" aria-label="menu" 
        aria-expanded="false" data-target="navbarBasicExample" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>

      </div>

      <div id="navbarBasicExample" class="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        
        <div class="navbar-start">
          
          <!-- search -->
          <form method="GET" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input class="input" type="text" placeholder="What are you looking for?" name="query" style="margin-top:8px">
              </div>

              <div class="control">
                <button class="button is-success" style="margin-top:8px">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                </button>
              </div>
            </div>
          </form>
          
        </div>

        <div class="navbar-end">

          <a href="/summer" class="navbar-item">Summer</a>
          <a  href="/winter" class="navbar-item">Winter</a>
          
          <div class="navbar-item">
            <div class="buttons">


              <template v-if="$store.state.isAuthenticated">
                  <router-link to="/my-account" class="button is-light">My Account</router-link>
              </template>

              <template v-else>
                <router-link to="/sign-up" class="button is-primary">Sign up</router-link>
                <router-link to="/log-in" class="button is-info">Log in</router-link>
              </template>
              
              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <i class="fas fa-shopping-cart"></i> ({{ cartTotalLength }})
                </span>
              </router-link>

            </div>
          </div>
        </div>

      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-right"></div>
    </div>

    <!-- body -->
    <section class="section">
      <router-view/>
    </section>

    <!-- footer -->
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    // initialize
    this.$store.commit('initiallizeStore')
    
    const token = this.$store.state.token

    if(token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }

  },
  mounted() {
      this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
.lds-dual-ring {
  display: inline-block;
  width:80px;
  height:80px;
}
.lds-dual-ring::after {
  content:"";
  display: block;
  width:64px;
  height: 64px;
  margin:8px;
  border-radius: 50%;
  border-color: 6px solid #ccc;
  animation: lds-dual-ring 1.2s liner infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg)
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height:0;
  overflow: hidden;
  --webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height:80px;
  }
}
</style>

