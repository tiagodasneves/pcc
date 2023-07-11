$(document).ready(function() {
    // Array para armazenar os depoimentos
    var testimonials = [];
  
    // Evento de envio do formulário
    $('#testimonial-form').submit(function(event) {
      event.preventDefault();
      var name = $('#name').val();
      var testimonial = $('#testimonial').val();
  
      // Adiciona o depoimento ao array
      testimonials.push({ name: name, testimonial: testimonial });
  
      // Limpa os campos do formulário
      $('#name').val('');
      $('#testimonial').val('');
  
      // Renderiza os depoimentos
      renderTestimonials();
    });
  
    // Função para renderizar os depoimentos
    function renderTestimonials() {
      $('#testimonial-list').empty();
      for (var i = 0; i < testimonials.length; i++) {
        var testimonial = testimonials[i];
        var testimonialHTML = `
          <div class="testimonial">
            <div class="name">${testimonial.name}</div>
            <div class="testimonial-text">${testimonial.testimonial}</div>
            <button class="btn btn-sm btn-danger delete-button" data-index="${i}">Excluir</button>
          </div>
        `;
        $('#testimonial-list').append(testimonialHTML);
      }
    }
  
    // Evento de clique no botão de exclusão
    $('#testimonial-list').on('click', '.delete-button', function() {
      var index = $(this).data('index');
      testimonials.splice(index, 1);
      renderTestimonials();
    });
  });
  