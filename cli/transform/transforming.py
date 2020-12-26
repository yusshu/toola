class TransformError(RuntimeError):

    def __init__(self, message: str):
        self.message = message
        RuntimeError.__init__(self, message)


class ArgumentTransformer:

    def transform(self, args: list[str]) -> object:
        raise NotImplementedError('The transform(...) function must be overwritten!')


class StringTransformer(ArgumentTransformer):

    def transform(self, args: list[str]) -> object:
        return ' '.join(args)


class IntegerTransformer(ArgumentTransformer):

    def transform(self, args: list[str]) -> object:
        arg = args[0]
        try:
            return int(arg)
        except ValueError:
            raise TransformError(f'The argument {arg} is not an integer!')


class BooleanTransformer(ArgumentTransformer):

    truthy_values = {'true', 'yes', 'y', '1', 'ok', 'accept'}
    falsy_values = {'false', 'no', 'n', '0', 'deny'}

    def transform(self, args: list[str]) -> object:
        arg = args[0]

        if arg in BooleanTransformer.truthy_values:
            return True
        elif arg in BooleanTransformer.falsy_values:
            return False

        raise TransformError(f'Argument {arg} is not a true or false value!')


transformers = dict[str, ArgumentTransformer]()

transformers['bool'] = BooleanTransformer()
transformers['int'] = IntegerTransformer()
transformers['str'] = StringTransformer()
