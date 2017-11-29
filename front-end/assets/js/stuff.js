$('#myModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})

$('#signUpButton').on('click', function (event) {
	console.log('clicked signUpButton');
	$('#thankYouModal').modal('show'); 
})


$('#sendButton').on('click', function (event) {
	console.log('clicked sendButton')
	$('#thankYouHandHoldModal').modal('show');
	//show new modal here
})