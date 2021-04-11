<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Ecommerce</p>
        <p class="subtitle">The best product store online</p>
      </div>
    </section>

    <div class="columns is-multiline">
      
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      
      <div class="column is-3" v-for="product in lastestProducts" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src=" 'http://127.0.0.1:8000' + product.get_thumbnail" alt="">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ product.price }}</p>

          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Detail</router-link>

        </div>
      </div>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      lastestProducts: []
    }
  },
  components: {
    
  },
  mounted() {
    this.getLastestProducts()
    document.title = 'Home | Ecommerce Store'
  },
  methods: {
    async getLastestProducts() {
      this.$store.commit('setIsLoading', true)

      await  axios.get('/api/v1/products/latest')
      .then(response => {
        this.lastestProducts = response.data
      })
      .catch( error => {
        console.log(error)
      })
      
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
