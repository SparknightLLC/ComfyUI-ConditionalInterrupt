import nodes


class AnyType(str):

	def __ne__(self, __value: object) -> bool:
		return False


any_type = AnyType("*")


class ConditionalInterrupt:
	"""Interrupt processing if the boolean input is true. Pass through the other input."""

	@classmethod
	def INPUT_TYPES(cls):
		return {
		    "required": {
		        "proceed": ("BOOLEAN", {
		            "default": True
		        }),
		        "input": (any_type, ),
		    },
		    "optional": {
		        "delay_helper": (any_type)
		    }
		}

	RETURN_TYPES = (any_type, )
	RETURN_NAMES = ("output", )
	FUNCTION = "doit"
	CATEGORY = "utils"

	def doit(self, proceed, input, delay_helper=None):
		if not proceed:
			nodes.interrupt_processing()

		return (input, )


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Conditional Interrupt": ConditionalInterrupt,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ConditionalInterrupt": "Conditional Interrupt",
}
