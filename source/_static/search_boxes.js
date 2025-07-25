const osbsearch = 'https://github.com/search?q=org%3AOpenSourceBrain+AND+%28path%3A*xml+OR+path%3A*nml+OR+path%3A*py%29+';
const nmldbsearch = 'https://neuroml-db.org/search_model?q=';

document.addEventListener('DOMContentLoaded', function (){
  const allForms = document.querySelectorAll("form.sharing-custom-search-form");

  allForms.forEach(form => {

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      const queryInput = this.querySelector('input[type="search"]');
      const query = queryInput ? encodeURIComponent(queryInput.value) : '';

      const sourceInput = this.querySelector('input[type="hidden"][name="source"]');
      const source = sourceInput ? sourceInput.value: "Unknown";

      let url;
      let win;

      switch (source) {
        case "osb":
          url = osbsearch + query + '&type=code';
          window.open(url, '_self');
          break;

        case "nmldb":
          url = nmldbsearch + query;
          window.open(url, '_blank');
          break;

        default:
          break;

      }
    })
  })

})
