class HTTPStatus:


    def __init__(self, code, description):
        self.code = int(code)
        self.description = str(description)
    
    def __lt__(self, other):
        try:
            other_code = other.code
        except AttributeError:
            other_code = other
        return self.code < other_code
    
    def __le__(self, other):
        return self < other or self == other
    
    def __eq__(self, other):
        try:
            other_code = other.code
        except AttributeError:
            other_code = other
        return self.code == other_code
    
    def __ne__(self, other):
        return not self == other
    
    def __gt__(self, other):
        try:
            other_code = other.code
        except AttributeError:
            other_code = other
        return self.code > other_code
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __int__(self):
        return self.code
    
    def __str__(self):
        return "HTTP {} - {}".format(self.code, self.description)
    
    def __repr__(self):
        return "HTTPStatus('%s',%d)" % (self.description, self.code)

def is_informational(status):
    return 100 <= status <= 199

def is_success(status):
    return 200 <= status <= 299

def is_redirect(status):
    return 300 <= status <= 399

def is_client_error(status):
    return 400 <= status <= 499

def is_server_error(status):
    return 500 <= status <= 599


HTTP_100_CONTINUE = HTTPStatus(100, 'Continue')
HTTP_101_SWITCHING_PROTOCOLS = HTTPStatus(101, 'Switching Protocols')
HTTP_102_PROCESSING = HTTPStatus(102, 'Processing')

HTTP_200_OK = HTTPStatus(200, 'OK')
HTTP_201_CREATED = HTTPStatus(201, 'Created')
HTTP_202_ACCEPTED = HTTPStatus(202, 'Accepted')
HTTP_203_NON_AUTHORITATIVE_INFORMATION = HTTPStatus(203, 'Non-Authoritative Information')
HTTP_204_NO_CONTENT = HTTPStatus(204, 'No Content')
HTTP_205_RESET_CONTENT = HTTPStatus(205, 'Reset Content')
HTTP_206_PARTIAL_CONTENT = HTTPStatus(206, 'Partial Content')
HTTP_207_MULTI_HTTPStatus = HTTPStatus(207, 'Multi-HTTPStatus')
HTTP_208_ALREADY_REPORTED = HTTPStatus(208, 'Already Reported')
HTTP_226_IM_USED = HTTPStatus(226, 'IM Used')

HTTP_300_MULTIPLE_CHOICES = HTTPStatus(300, 'Multiple Choices')
HTTP_301_MOVED_PERMANENTLY = HTTPStatus(301, 'Moved Permanently')
HTTP_302_FOUND = HTTPStatus(302, 'Found')
HTTP_303_SEE_OTHER = HTTPStatus(303, 'See Other')
HTTP_304_NOT_MODIFIED = HTTPStatus(304, 'Not Modified')
HTTP_305_USE_PROXY = HTTPStatus(305, 'Use Proxy')
HTTP_306_SWITCH_PROXY = HTTPStatus(306, 'Switch Proxy')
HTTP_307_TEMPORARY_REDIRECT = HTTPStatus(307, 'Temporary Redirect')
HTTP_308_PERMANENT_REDIRECT = HTTPStatus(308, 'Permanent Redirect')

HTTP_400_BAD_REQUEST = HTTPStatus(400, 'Bad Request')
HTTP_401_UNAUTHORIZED = HTTPStatus(401, 'Unauthorized')
HTTP_402_PAYMENT_REQUIRED = HTTPStatus(402, 'Payment Required')
HTTP_403_FORBIDDEN = HTTPStatus(403, 'Forbidden')
HTTP_404_NOT_FOUND = HTTPStatus(404, 'Not Found')
HTTP_405_METHOD_NOT_ALLOWED = HTTPStatus(405, 'Method Not Allowed')
HTTP_406_NOT_ACCEPTABLE = HTTPStatus(406, 'Not Acceptable')
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = HTTPStatus(407, 'Proxy Authentication Required')
HTTP_408_REQUEST_TIMEOUT = HTTPStatus(408, 'Request Timeout')
HTTP_409_CONFLICT = HTTPStatus(409, 'Conflict')
HTTP_410_GONE = HTTPStatus(410, 'Gone')
HTTP_411_LENGTH_REQUIRED = HTTPStatus(411, 'Length Required')
HTTP_412_PRECONDITION_FAILED = HTTPStatus(412, 'Precondition Failed')
HTTP_413_PAYLOAD_TOO_LARGE = HTTPStatus(413, 'Payload Too Large')
HTTP_414_URI_TOO_LONG = HTTPStatus(414, 'URI Too Long')
HTTP_415_UNSUPPORTED_MEDIA_TYPE = HTTPStatus(415, 'Unsupported Media Type')
HTTP_416_RANGE_NOT_SATISFIABLE = HTTPStatus(416, 'Range Not Satisfiable')
HTTP_417_EXPECTATION_FAILED = HTTPStatus(417, 'Expectation Failed')
HTTP_418_I_AM_A_TEAPOT = HTTPStatus(418, "I'm a teapot")
HTTP_419_AUTHENTICATION_TIMEOUT = HTTPStatus(419, 'Authentication Timeout')
HTTP_421_MISDIRECTED_REQUEST = HTTPStatus(421, 'Misdirected Request')
HTTP_422_UNPROCESSABLE_ENTITY = HTTPStatus(422, 'Unprocessable Entity')
HTTP_423_LOCKED = HTTPStatus(423, 'Locked')
HTTP_424_FAILED_DEPENDENCY = HTTPStatus(424, 'Failed Dependency')
HTTP_426_UPGRADE_REQUIRED = HTTPStatus(426, 'Upgrade Required')
HTTP_428_PRECONDITION_REQUIRED = HTTPStatus(428, 'Precondition Required')
HTTP_429_TOO_MANY_REQUESTS = HTTPStatus(429, 'Too Many Requests')
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = HTTPStatus(431, 'Request Header Fields Too Large')
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = HTTPStatus(451, 'Unavailable For Legal Reasons')

HTTP_500_INTERNAL_SERVER_ERROR = HTTPStatus(500, 'Internal Server Error')
HTTP_501_NOT_IMPLEMENTED = HTTPStatus(501, 'Not Implemented')
HTTP_502_BAD_GATEWAY = HTTPStatus(502, 'Bad Gateway')
HTTP_503_SERVICE_UNAVAILABLE = HTTPStatus(503, 'Service Unavailable')
HTTP_504_GATEWAY_TIMEOUT = HTTPStatus(504, 'Gateway Timeout')
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = HTTPStatus(505, 'HTTP Version Not Supported')
HTTP_506_VARIANT_ALSO_NEGOTIATES = HTTPStatus(506, 'Variant Also Negotiates')
HTTP_507_INSUFFICIENT_STORAGE = HTTPStatus(507, 'Insufficient Storage')
HTTP_508_LOOP_DETECTED = HTTPStatus(508, 'Loop Detected')
HTTP_510_NOT_EXTENDED = HTTPStatus(510, 'Not Extended')
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = HTTPStatus(511, 'Natwork Authentication Required')
