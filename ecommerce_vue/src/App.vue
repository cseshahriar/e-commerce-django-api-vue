<template>
  <div class="wrapper">
    
    <!-- navbar -->
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
        </a>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
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
                  <i class="fas fa-shopping-cart"></i>
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

<style lang="scss">
@import '../node_modules/bulma';
</style>
