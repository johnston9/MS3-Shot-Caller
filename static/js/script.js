/*jQuery for Materialize initialization of the sidenav, collapsible, tooltipped,
  modal, select and datepicker features*/

$(document).ready(function () {
    setTimeout(function() {
    $('.flashes').fadeOut('fast');
    }, 5000);
	$('.sidenav').sidenav({
		edge: "right"
	});
	$('.collapsible').collapsible();
	$('.tooltipped').tooltip();
	$('select').formSelect();
	$('.modal').modal();
	$(".datepicker").datepicker({
		format: "dd mmmm, yyyy",
		yearRange: 3,
		showClearBtn: true,
		i18n: {
			done: "Select"
		}
	});

    /* Function to fix Materialize bug to show red line warning if department not 
       selected in add message*/

	validateMaterializeSelect();

	function validateMaterializeSelect() {
		let classValid = {
			"border-bottom": "1px solid #4caf50",
			"box-shadow": "0 1px 0 0 #4caf50"
		};
		let classInvalid = {
			"border-bottom": "1px solid #f44336",
			"box-shadow": "0 1px 0 0 #f44336"
		};
		if ($("select.validate").prop("required")) {
			$("select.validate").css({
				"display": "block",
				"height": "0",
				"padding": "0",
				"width": "0",
				"position": "absolute"
			});
		}
		$(".select-wrapper input.select-dropdown").on("focusin", function () {
			$(this).parent(".select-wrapper").on("change", function () {
				if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
					$(this).children("input").css(classValid);
				}
			});
		}).on("click", function () {
			if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
				$(this).parent(".select-wrapper").children("input").css(classValid);
			} else {
				$(".select-wrapper input.select-dropdown").on("focusout", function () {
					if ($(this).parent(".select-wrapper").children("select").prop("required")) {
						if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
							$(this).parent(".select-wrapper").children("input").css(classInvalid);
						}
					}
				});
			}
		});
	}
});

/*-----function to create the return to top button-----*/

const topbutton = document.getElementById("topbut");

topbutton.addEventListener("click", poptop);

window.onscroll = function () {
	buttonDisplay();
};

function buttonDisplay() {
	if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
		topbutton.style.display = "block";
	} else {
		topbutton.style.display = "none";
	}
}

function poptop() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}


/*-----function to give image not loading error for admin-----*/

function image_error() {
    document.getElementById("image-er").innerText = "Available Soon" ;
}



