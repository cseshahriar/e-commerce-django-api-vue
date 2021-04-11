<template>
  <div class="wrapper">
    
    <!-- navbar -->
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
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
          <a class="navbar-item">Summer</a>
          <a class="navbar-item">Winter</a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/signup" class="button is-primary">
                <span class="icon">
                  <i class="fas fa-user-plus"></i>
                </span>
                </router-link>
              <router-link to="/log-in" class="button is-info">
                <span class="icon">
                  <i class="fas fa-sign-in-alt"></i>
                </span>
              </router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <i class="fas fa-shopping-cart"></i> ({{ cartTotalLength }})
                </span>
              </router-link>
              <router-link to="/logout" class="button is-danger">
                <span class="icon">
                  <i class="fas fa-sign-out-alt"></i>
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
    this.$store.commit('initiallizeStore')
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

