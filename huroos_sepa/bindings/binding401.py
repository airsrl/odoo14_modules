# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a34f18d1847e9975aa09f4e612454f2420da94cc
# Generated 2024-04-30 13:52:42.688161 by PyXB version 1.2.6 using Python 3.10.12.final.0
# Namespace urn:CBI:xsd:CBIPaymentRequest.00.04.01

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6c0807b5-7822-45f1-82ca-68bc5d4c7f33')

# Version of PyXB used to generate the bindings
#_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:CBI:xsd:CBIPaymentRequest.00.04.01', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 437, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.INF = STD_ANON._CF_enumeration.addEnumeration(unicode_value='INF', tag='INF')
STD_ANON.SNR = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SNR', tag='SNR')
STD_ANON.CVA = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CVA', tag='CVA')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIActiveOrHistoricCurrencyAndAmount_SimpleType
class CBIActiveOrHistoricCurrencyAndAmount_SimpleType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIActiveOrHistoricCurrencyAndAmount_SimpleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 886, 1)
    _Documentation = None
CBIActiveOrHistoricCurrencyAndAmount_SimpleType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
CBIActiveOrHistoricCurrencyAndAmount_SimpleType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.decimal('0.0'), value_datatype=CBIActiveOrHistoricCurrencyAndAmount_SimpleType)
CBIActiveOrHistoricCurrencyAndAmount_SimpleType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
CBIActiveOrHistoricCurrencyAndAmount_SimpleType._InitializeFacetMap(CBIActiveOrHistoricCurrencyAndAmount_SimpleType._CF_fractionDigits,
   CBIActiveOrHistoricCurrencyAndAmount_SimpleType._CF_minInclusive,
   CBIActiveOrHistoricCurrencyAndAmount_SimpleType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'CBIActiveOrHistoricCurrencyAndAmount_SimpleType', CBIActiveOrHistoricCurrencyAndAmount_SimpleType)
_module_typeBindings.CBIActiveOrHistoricCurrencyAndAmount_SimpleType = CBIActiveOrHistoricCurrencyAndAmount_SimpleType

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ActiveOrHistoricCurrencyCode
class ActiveOrHistoricCurrencyCode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 893, 1)
    _Documentation = None
ActiveOrHistoricCurrencyCode._CF_pattern = pyxb.binding.facets.CF_pattern()
ActiveOrHistoricCurrencyCode._CF_pattern.addPattern(pattern='[A-Z]{3,3}')
ActiveOrHistoricCurrencyCode._InitializeFacetMap(ActiveOrHistoricCurrencyCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyCode', ActiveOrHistoricCurrencyCode)
_module_typeBindings.ActiveOrHistoricCurrencyCode = ActiveOrHistoricCurrencyCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AddressType2Code
class AddressType2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType2Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 898, 1)
    _Documentation = None
AddressType2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=AddressType2Code)
AddressType2Code.ADDR = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='ADDR', tag='ADDR')
AddressType2Code.PBOX = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='PBOX', tag='PBOX')
AddressType2Code.HOME = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='HOME', tag='HOME')
AddressType2Code.BIZZ = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='BIZZ', tag='BIZZ')
AddressType2Code.MLTO = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='MLTO', tag='MLTO')
AddressType2Code.DLVY = AddressType2Code._CF_enumeration.addEnumeration(unicode_value='DLVY', tag='DLVY')
AddressType2Code._InitializeFacetMap(AddressType2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AddressType2Code', AddressType2Code)
_module_typeBindings.AddressType2Code = AddressType2Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AnyBICDec2014Identifier
class AnyBICDec2014Identifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyBICDec2014Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 908, 1)
    _Documentation = None
AnyBICDec2014Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
AnyBICDec2014Identifier._CF_pattern.addPattern(pattern='[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}')
AnyBICDec2014Identifier._InitializeFacetMap(AnyBICDec2014Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AnyBICDec2014Identifier', AnyBICDec2014Identifier)
_module_typeBindings.AnyBICDec2014Identifier = AnyBICDec2014Identifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BatchBookingIndicator
class BatchBookingIndicator (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BatchBookingIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 913, 1)
    _Documentation = None
BatchBookingIndicator._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BatchBookingIndicator', BatchBookingIndicator)
_module_typeBindings.BatchBookingIndicator = BatchBookingIndicator

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BICFIDec2014Identifier
class BICFIDec2014Identifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BICFIDec2014Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 916, 1)
    _Documentation = None
BICFIDec2014Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
BICFIDec2014Identifier._CF_pattern.addPattern(pattern='[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}')
BICFIDec2014Identifier._InitializeFacetMap(BICFIDec2014Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BICFIDec2014Identifier', BICFIDec2014Identifier)
_module_typeBindings.BICFIDec2014Identifier = BICFIDec2014Identifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIChargeBearerTypeCode
class CBIChargeBearerTypeCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIChargeBearerTypeCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 921, 1)
    _Documentation = None
CBIChargeBearerTypeCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CBIChargeBearerTypeCode)
CBIChargeBearerTypeCode.SLEV = CBIChargeBearerTypeCode._CF_enumeration.addEnumeration(unicode_value='SLEV', tag='SLEV')
CBIChargeBearerTypeCode._InitializeFacetMap(CBIChargeBearerTypeCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIChargeBearerTypeCode', CBIChargeBearerTypeCode)
_module_typeBindings.CBIChargeBearerTypeCode = CBIChargeBearerTypeCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIChequeType1Code
class CBIChequeType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIChequeType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 926, 1)
    _Documentation = None
CBIChequeType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CBIChequeType1Code)
CBIChequeType1Code.CCCH = CBIChequeType1Code._CF_enumeration.addEnumeration(unicode_value='CCCH', tag='CCCH')
CBIChequeType1Code.BCHQ = CBIChequeType1Code._CF_enumeration.addEnumeration(unicode_value='BCHQ', tag='BCHQ')
CBIChequeType1Code._InitializeFacetMap(CBIChequeType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIChequeType1Code', CBIChequeType1Code)
_module_typeBindings.CBIChequeType1Code = CBIChequeType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRegulatoryReportingType1Code
class CBIRegulatoryReportingType1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRegulatoryReportingType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 932, 1)
    _Documentation = None
CBIRegulatoryReportingType1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CBIRegulatoryReportingType1Code)
CBIRegulatoryReportingType1Code.DEBT = CBIRegulatoryReportingType1Code._CF_enumeration.addEnumeration(unicode_value='DEBT', tag='DEBT')
CBIRegulatoryReportingType1Code._InitializeFacetMap(CBIRegulatoryReportingType1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIRegulatoryReportingType1Code', CBIRegulatoryReportingType1Code)
_module_typeBindings.CBIRegulatoryReportingType1Code = CBIRegulatoryReportingType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRemittanceLocationMethod1Code
class CBIRemittanceLocationMethod1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRemittanceLocationMethod1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 937, 1)
    _Documentation = None
CBIRemittanceLocationMethod1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CBIRemittanceLocationMethod1Code)
CBIRemittanceLocationMethod1Code.FAXI = CBIRemittanceLocationMethod1Code._CF_enumeration.addEnumeration(unicode_value='FAXI', tag='FAXI')
CBIRemittanceLocationMethod1Code.EMAL = CBIRemittanceLocationMethod1Code._CF_enumeration.addEnumeration(unicode_value='EMAL', tag='EMAL')
CBIRemittanceLocationMethod1Code.SMSM = CBIRemittanceLocationMethod1Code._CF_enumeration.addEnumeration(unicode_value='SMSM', tag='SMSM')
CBIRemittanceLocationMethod1Code._InitializeFacetMap(CBIRemittanceLocationMethod1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIRemittanceLocationMethod1Code', CBIRemittanceLocationMethod1Code)
_module_typeBindings.CBIRemittanceLocationMethod1Code = CBIRemittanceLocationMethod1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIServiceLevel1Code
class CBIServiceLevel1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIServiceLevel1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 944, 1)
    _Documentation = None
CBIServiceLevel1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CBIServiceLevel1Code)
CBIServiceLevel1Code.SEPA = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='SEPA', tag='SEPA')
CBIServiceLevel1Code.URGP = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='URGP', tag='URGP')
CBIServiceLevel1Code.FAST = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='FAST', tag='FAST')
CBIServiceLevel1Code.PGPA = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='PGPA', tag='PGPA')
CBIServiceLevel1Code.PGSP = CBIServiceLevel1Code._CF_enumeration.addEnumeration(unicode_value='PGSP', tag='PGSP')
CBIServiceLevel1Code._InitializeFacetMap(CBIServiceLevel1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBIServiceLevel1Code', CBIServiceLevel1Code)
_module_typeBindings.CBIServiceLevel1Code = CBIServiceLevel1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBISrvInf1
class CBISrvInf1 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBISrvInf1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 953, 1)
    _Documentation = None
CBISrvInf1._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CBISrvInf1)
CBISrvInf1.ESBEN = CBISrvInf1._CF_enumeration.addEnumeration(unicode_value='ESBEN', tag='ESBEN')
CBISrvInf1._InitializeFacetMap(CBISrvInf1._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CBISrvInf1', CBISrvInf1)
_module_typeBindings.CBISrvInf1 = CBISrvInf1

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CountryCode
class CountryCode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 958, 1)
    _Documentation = None
CountryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCode._CF_pattern.addPattern(pattern='[A-Z]{2,2}')
CountryCode._InitializeFacetMap(CountryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountryCode', CountryCode)
_module_typeBindings.CountryCode = CountryCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditDebitCode
class CreditDebitCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditDebitCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 963, 1)
    _Documentation = None
CreditDebitCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CreditDebitCode)
CreditDebitCode.CRDT = CreditDebitCode._CF_enumeration.addEnumeration(unicode_value='CRDT', tag='CRDT')
CreditDebitCode.DBIT = CreditDebitCode._CF_enumeration.addEnumeration(unicode_value='DBIT', tag='DBIT')
CreditDebitCode._InitializeFacetMap(CreditDebitCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CreditDebitCode', CreditDebitCode)
_module_typeBindings.CreditDebitCode = CreditDebitCode

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIDecimalNumber
class CBIDecimalNumber (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIDecimalNumber')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 969, 1)
    _Documentation = None
CBIDecimalNumber._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
CBIDecimalNumber._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
CBIDecimalNumber._InitializeFacetMap(CBIDecimalNumber._CF_fractionDigits,
   CBIDecimalNumber._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'CBIDecimalNumber', CBIDecimalNumber)
_module_typeBindings.CBIDecimalNumber = CBIDecimalNumber

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DecimalNumber
class DecimalNumber (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DecimalNumber')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 975, 1)
    _Documentation = None
DecimalNumber._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(17))
DecimalNumber._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
DecimalNumber._InitializeFacetMap(DecimalNumber._CF_fractionDigits,
   DecimalNumber._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'DecimalNumber', DecimalNumber)
_module_typeBindings.DecimalNumber = DecimalNumber

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentType3Code
class DocumentType3Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentType3Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 981, 1)
    _Documentation = None
DocumentType3Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=DocumentType3Code)
DocumentType3Code.RADM = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='RADM', tag='RADM')
DocumentType3Code.RPIN = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='RPIN', tag='RPIN')
DocumentType3Code.FXDR = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='FXDR', tag='FXDR')
DocumentType3Code.DISP = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='DISP', tag='DISP')
DocumentType3Code.PUOR = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='PUOR', tag='PUOR')
DocumentType3Code.SCOR = DocumentType3Code._CF_enumeration.addEnumeration(unicode_value='SCOR', tag='SCOR')
DocumentType3Code._InitializeFacetMap(DocumentType3Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DocumentType3Code', DocumentType3Code)
_module_typeBindings.DocumentType3Code = DocumentType3Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentType6Code
class DocumentType6Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentType6Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 991, 1)
    _Documentation = None
DocumentType6Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=DocumentType6Code)
DocumentType6Code.MSIN = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='MSIN', tag='MSIN')
DocumentType6Code.CNFA = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='CNFA', tag='CNFA')
DocumentType6Code.DNFA = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='DNFA', tag='DNFA')
DocumentType6Code.CINV = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='CINV', tag='CINV')
DocumentType6Code.CREN = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='CREN', tag='CREN')
DocumentType6Code.DEBN = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='DEBN', tag='DEBN')
DocumentType6Code.HIRI = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='HIRI', tag='HIRI')
DocumentType6Code.SBIN = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='SBIN', tag='SBIN')
DocumentType6Code.CMCN = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='CMCN', tag='CMCN')
DocumentType6Code.SOAC = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='SOAC', tag='SOAC')
DocumentType6Code.DISP = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='DISP', tag='DISP')
DocumentType6Code.BOLD = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='BOLD', tag='BOLD')
DocumentType6Code.VCHR = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='VCHR', tag='VCHR')
DocumentType6Code.AROI = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='AROI', tag='AROI')
DocumentType6Code.TSUT = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='TSUT', tag='TSUT')
DocumentType6Code.PUOR = DocumentType6Code._CF_enumeration.addEnumeration(unicode_value='PUOR', tag='PUOR')
DocumentType6Code._InitializeFacetMap(DocumentType6Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DocumentType6Code', DocumentType6Code)
_module_typeBindings.DocumentType6Code = DocumentType6Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Exact4AlphaNumericText
class Exact4AlphaNumericText (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Exact4AlphaNumericText')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1011, 1)
    _Documentation = None
Exact4AlphaNumericText._CF_pattern = pyxb.binding.facets.CF_pattern()
Exact4AlphaNumericText._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{4}')
Exact4AlphaNumericText._InitializeFacetMap(Exact4AlphaNumericText._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Exact4AlphaNumericText', Exact4AlphaNumericText)
_module_typeBindings.Exact4AlphaNumericText = Exact4AlphaNumericText

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalCashAccountType1Code
class ExternalCashAccountType1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalCashAccountType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1016, 1)
    _Documentation = None
ExternalCashAccountType1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalCashAccountType1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalCashAccountType1Code._InitializeFacetMap(ExternalCashAccountType1Code._CF_maxLength,
   ExternalCashAccountType1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalCashAccountType1Code', ExternalCashAccountType1Code)
_module_typeBindings.ExternalCashAccountType1Code = ExternalCashAccountType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalCategoryPurpose1Code
class ExternalCategoryPurpose1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalCategoryPurpose1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1022, 1)
    _Documentation = None
ExternalCategoryPurpose1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalCategoryPurpose1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalCategoryPurpose1Code._InitializeFacetMap(ExternalCategoryPurpose1Code._CF_maxLength,
   ExternalCategoryPurpose1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalCategoryPurpose1Code', ExternalCategoryPurpose1Code)
_module_typeBindings.ExternalCategoryPurpose1Code = ExternalCategoryPurpose1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalDiscountAmountType1Code
class ExternalDiscountAmountType1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalDiscountAmountType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1028, 1)
    _Documentation = None
ExternalDiscountAmountType1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalDiscountAmountType1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalDiscountAmountType1Code._InitializeFacetMap(ExternalDiscountAmountType1Code._CF_maxLength,
   ExternalDiscountAmountType1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalDiscountAmountType1Code', ExternalDiscountAmountType1Code)
_module_typeBindings.ExternalDiscountAmountType1Code = ExternalDiscountAmountType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalDocumentLineType1Code
class ExternalDocumentLineType1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalDocumentLineType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1034, 1)
    _Documentation = None
ExternalDocumentLineType1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalDocumentLineType1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalDocumentLineType1Code._InitializeFacetMap(ExternalDocumentLineType1Code._CF_maxLength,
   ExternalDocumentLineType1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalDocumentLineType1Code', ExternalDocumentLineType1Code)
_module_typeBindings.ExternalDocumentLineType1Code = ExternalDocumentLineType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalGarnishmentType1Code
class ExternalGarnishmentType1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalGarnishmentType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1040, 1)
    _Documentation = None
ExternalGarnishmentType1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalGarnishmentType1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalGarnishmentType1Code._InitializeFacetMap(ExternalGarnishmentType1Code._CF_maxLength,
   ExternalGarnishmentType1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalGarnishmentType1Code', ExternalGarnishmentType1Code)
_module_typeBindings.ExternalGarnishmentType1Code = ExternalGarnishmentType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalLocalInstrument1Code
class ExternalLocalInstrument1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalLocalInstrument1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1046, 1)
    _Documentation = None
ExternalLocalInstrument1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
ExternalLocalInstrument1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalLocalInstrument1Code._InitializeFacetMap(ExternalLocalInstrument1Code._CF_maxLength,
   ExternalLocalInstrument1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalLocalInstrument1Code', ExternalLocalInstrument1Code)
_module_typeBindings.ExternalLocalInstrument1Code = ExternalLocalInstrument1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalOrganisationIdentification1Code
class ExternalOrganisationIdentification1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalOrganisationIdentification1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1052, 1)
    _Documentation = None
ExternalOrganisationIdentification1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalOrganisationIdentification1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalOrganisationIdentification1Code._InitializeFacetMap(ExternalOrganisationIdentification1Code._CF_maxLength,
   ExternalOrganisationIdentification1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalOrganisationIdentification1Code', ExternalOrganisationIdentification1Code)
_module_typeBindings.ExternalOrganisationIdentification1Code = ExternalOrganisationIdentification1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalPersonIdentification1Code
class ExternalPersonIdentification1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalPersonIdentification1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1058, 1)
    _Documentation = None
ExternalPersonIdentification1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalPersonIdentification1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalPersonIdentification1Code._InitializeFacetMap(ExternalPersonIdentification1Code._CF_maxLength,
   ExternalPersonIdentification1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalPersonIdentification1Code', ExternalPersonIdentification1Code)
_module_typeBindings.ExternalPersonIdentification1Code = ExternalPersonIdentification1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalPurpose1Code
class ExternalPurpose1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalPurpose1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1064, 1)
    _Documentation = None
ExternalPurpose1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalPurpose1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalPurpose1Code._InitializeFacetMap(ExternalPurpose1Code._CF_maxLength,
   ExternalPurpose1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalPurpose1Code', ExternalPurpose1Code)
_module_typeBindings.ExternalPurpose1Code = ExternalPurpose1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ExternalTaxAmountType1Code
class ExternalTaxAmountType1Code (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalTaxAmountType1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1070, 1)
    _Documentation = None
ExternalTaxAmountType1Code._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
ExternalTaxAmountType1Code._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
ExternalTaxAmountType1Code._InitializeFacetMap(ExternalTaxAmountType1Code._CF_maxLength,
   ExternalTaxAmountType1Code._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'ExternalTaxAmountType1Code', ExternalTaxAmountType1Code)
_module_typeBindings.ExternalTaxAmountType1Code = ExternalTaxAmountType1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Instruction3Code
class Instruction3Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Instruction3Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1076, 1)
    _Documentation = None
Instruction3Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=Instruction3Code)
Instruction3Code.CHQB = Instruction3Code._CF_enumeration.addEnumeration(unicode_value='CHQB', tag='CHQB')
Instruction3Code.HOLD = Instruction3Code._CF_enumeration.addEnumeration(unicode_value='HOLD', tag='HOLD')
Instruction3Code.PHOB = Instruction3Code._CF_enumeration.addEnumeration(unicode_value='PHOB', tag='PHOB')
Instruction3Code.TELB = Instruction3Code._CF_enumeration.addEnumeration(unicode_value='TELB', tag='TELB')
Instruction3Code._InitializeFacetMap(Instruction3Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Instruction3Code', Instruction3Code)
_module_typeBindings.Instruction3Code = Instruction3Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}IBAN2007Identifier
class IBAN2007Identifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IBAN2007Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1084, 1)
    _Documentation = None
IBAN2007Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
IBAN2007Identifier._CF_pattern.addPattern(pattern='[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}')
IBAN2007Identifier._InitializeFacetMap(IBAN2007Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'IBAN2007Identifier', IBAN2007Identifier)
_module_typeBindings.IBAN2007Identifier = IBAN2007Identifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ISODate
class ISODate (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODate')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1089, 1)
    _Documentation = None
ISODate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODate', ISODate)
_module_typeBindings.ISODate = ISODate

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ISODateTime
class ISODateTime (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODateTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1092, 1)
    _Documentation = None
ISODateTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODateTime', ISODateTime)
_module_typeBindings.ISODateTime = ISODateTime

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LEIIdentifier
class LEIIdentifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LEIIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1095, 1)
    _Documentation = None
LEIIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
LEIIdentifier._CF_pattern.addPattern(pattern='[A-Z0-9]{18,18}[0-9]{2,2}')
LEIIdentifier._InitializeFacetMap(LEIIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LEIIdentifier', LEIIdentifier)
_module_typeBindings.LEIIdentifier = LEIIdentifier

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max4Text
class Max4Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max4Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1100, 1)
    _Documentation = None
Max4Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
Max4Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max4Text._InitializeFacetMap(Max4Text._CF_maxLength,
   Max4Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max4Text', Max4Text)
_module_typeBindings.Max4Text = Max4Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max15NumericText
class Max15NumericText (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max15NumericText')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1106, 1)
    _Documentation = None
Max15NumericText._CF_pattern = pyxb.binding.facets.CF_pattern()
Max15NumericText._CF_pattern.addPattern(pattern='[0-9]{1,15}')
Max15NumericText._InitializeFacetMap(Max15NumericText._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Max15NumericText', Max15NumericText)
_module_typeBindings.Max15NumericText = Max15NumericText

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max16Text
class Max16Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max16Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1111, 1)
    _Documentation = None
Max16Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
Max16Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max16Text._InitializeFacetMap(Max16Text._CF_maxLength,
   Max16Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max16Text', Max16Text)
_module_typeBindings.Max16Text = Max16Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max35Text
class Max35Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1117, 1)
    _Documentation = None
Max35Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
Max35Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max35Text._InitializeFacetMap(Max35Text._CF_maxLength,
   Max35Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max35Text', Max35Text)
_module_typeBindings.Max35Text = Max35Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max70Text
class Max70Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max70Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1123, 1)
    _Documentation = None
Max70Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(70))
Max70Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max70Text._InitializeFacetMap(Max70Text._CF_maxLength,
   Max70Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max70Text', Max70Text)
_module_typeBindings.Max70Text = Max70Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max128Text
class Max128Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max128Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1129, 1)
    _Documentation = None
Max128Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(128))
Max128Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max128Text._InitializeFacetMap(Max128Text._CF_maxLength,
   Max128Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max128Text', Max128Text)
_module_typeBindings.Max128Text = Max128Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max140Text
class Max140Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max140Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1135, 1)
    _Documentation = None
Max140Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(140))
Max140Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max140Text._InitializeFacetMap(Max140Text._CF_maxLength,
   Max140Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max140Text', Max140Text)
_module_typeBindings.Max140Text = Max140Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max350Text
class Max350Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max350Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1141, 1)
    _Documentation = None
Max350Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(350))
Max350Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max350Text._InitializeFacetMap(Max350Text._CF_maxLength,
   Max350Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max350Text', Max350Text)
_module_typeBindings.Max350Text = Max350Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Max2048Text
class Max2048Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max2048Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1147, 1)
    _Documentation = None
Max2048Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2048))
Max2048Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max2048Text._InitializeFacetMap(Max2048Text._CF_maxLength,
   Max2048Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max2048Text', Max2048Text)
_module_typeBindings.Max2048Text = Max2048Text

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}NamePrefix2Code
class NamePrefix2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NamePrefix2Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1153, 1)
    _Documentation = None
NamePrefix2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=NamePrefix2Code)
NamePrefix2Code.DOCT = NamePrefix2Code._CF_enumeration.addEnumeration(unicode_value='DOCT', tag='DOCT')
NamePrefix2Code.MADM = NamePrefix2Code._CF_enumeration.addEnumeration(unicode_value='MADM', tag='MADM')
NamePrefix2Code.MISS = NamePrefix2Code._CF_enumeration.addEnumeration(unicode_value='MISS', tag='MISS')
NamePrefix2Code.MIST = NamePrefix2Code._CF_enumeration.addEnumeration(unicode_value='MIST', tag='MIST')
NamePrefix2Code.MIKS = NamePrefix2Code._CF_enumeration.addEnumeration(unicode_value='MIKS', tag='MIKS')
NamePrefix2Code._InitializeFacetMap(NamePrefix2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NamePrefix2Code', NamePrefix2Code)
_module_typeBindings.NamePrefix2Code = NamePrefix2Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Number
class Number (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Number')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1162, 1)
    _Documentation = None
Number._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0))
Number._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
Number._InitializeFacetMap(Number._CF_fractionDigits,
   Number._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'Number', Number)
_module_typeBindings.Number = Number

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PaymentMethod3Code
class PaymentMethod3Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentMethod3Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1168, 1)
    _Documentation = None
PaymentMethod3Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=PaymentMethod3Code)
PaymentMethod3Code.CHK = PaymentMethod3Code._CF_enumeration.addEnumeration(unicode_value='CHK', tag='CHK')
PaymentMethod3Code.TRF = PaymentMethod3Code._CF_enumeration.addEnumeration(unicode_value='TRF', tag='TRF')
PaymentMethod3Code.TRA = PaymentMethod3Code._CF_enumeration.addEnumeration(unicode_value='TRA', tag='TRA')
PaymentMethod3Code._InitializeFacetMap(PaymentMethod3Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PaymentMethod3Code', PaymentMethod3Code)
_module_typeBindings.PaymentMethod3Code = PaymentMethod3Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PercentageRate
class PercentageRate (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageRate')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1175, 1)
    _Documentation = None
PercentageRate._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(10))
PercentageRate._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11))
PercentageRate._InitializeFacetMap(PercentageRate._CF_fractionDigits,
   PercentageRate._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'PercentageRate', PercentageRate)
_module_typeBindings.PercentageRate = PercentageRate

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PreferredContactMethod1Code
class PreferredContactMethod1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PreferredContactMethod1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1181, 1)
    _Documentation = None
PreferredContactMethod1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=PreferredContactMethod1Code)
PreferredContactMethod1Code.LETT = PreferredContactMethod1Code._CF_enumeration.addEnumeration(unicode_value='LETT', tag='LETT')
PreferredContactMethod1Code.MAIL = PreferredContactMethod1Code._CF_enumeration.addEnumeration(unicode_value='MAIL', tag='MAIL')
PreferredContactMethod1Code.PHON = PreferredContactMethod1Code._CF_enumeration.addEnumeration(unicode_value='PHON', tag='PHON')
PreferredContactMethod1Code.FAXX = PreferredContactMethod1Code._CF_enumeration.addEnumeration(unicode_value='FAXX', tag='FAXX')
PreferredContactMethod1Code.CELL = PreferredContactMethod1Code._CF_enumeration.addEnumeration(unicode_value='CELL', tag='CELL')
PreferredContactMethod1Code._InitializeFacetMap(PreferredContactMethod1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PreferredContactMethod1Code', PreferredContactMethod1Code)
_module_typeBindings.PreferredContactMethod1Code = PreferredContactMethod1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Priority2Code
class Priority2Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Priority2Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1190, 1)
    _Documentation = None
Priority2Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=Priority2Code)
Priority2Code.HIGH = Priority2Code._CF_enumeration.addEnumeration(unicode_value='HIGH', tag='HIGH')
Priority2Code.NORM = Priority2Code._CF_enumeration.addEnumeration(unicode_value='NORM', tag='NORM')
Priority2Code._InitializeFacetMap(Priority2Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Priority2Code', Priority2Code)
_module_typeBindings.Priority2Code = Priority2Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PhoneNumber
class PhoneNumber (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhoneNumber')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1196, 1)
    _Documentation = None
PhoneNumber._CF_pattern = pyxb.binding.facets.CF_pattern()
PhoneNumber._CF_pattern.addPattern(pattern='\\+[0-9]{1,3}-[0-9()+\\-]{1,30}')
PhoneNumber._InitializeFacetMap(PhoneNumber._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'PhoneNumber', PhoneNumber)
_module_typeBindings.PhoneNumber = PhoneNumber

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxRecordPeriod1Code
class TaxRecordPeriod1Code (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxRecordPeriod1Code')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1201, 1)
    _Documentation = None
TaxRecordPeriod1Code._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TaxRecordPeriod1Code)
TaxRecordPeriod1Code.MM01 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM01', tag='MM01')
TaxRecordPeriod1Code.MM02 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM02', tag='MM02')
TaxRecordPeriod1Code.MM03 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM03', tag='MM03')
TaxRecordPeriod1Code.MM04 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM04', tag='MM04')
TaxRecordPeriod1Code.MM05 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM05', tag='MM05')
TaxRecordPeriod1Code.MM06 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM06', tag='MM06')
TaxRecordPeriod1Code.MM07 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM07', tag='MM07')
TaxRecordPeriod1Code.MM08 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM08', tag='MM08')
TaxRecordPeriod1Code.MM09 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM09', tag='MM09')
TaxRecordPeriod1Code.MM10 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM10', tag='MM10')
TaxRecordPeriod1Code.MM11 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM11', tag='MM11')
TaxRecordPeriod1Code.MM12 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='MM12', tag='MM12')
TaxRecordPeriod1Code.QTR1 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='QTR1', tag='QTR1')
TaxRecordPeriod1Code.QTR2 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='QTR2', tag='QTR2')
TaxRecordPeriod1Code.QTR3 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='QTR3', tag='QTR3')
TaxRecordPeriod1Code.QTR4 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='QTR4', tag='QTR4')
TaxRecordPeriod1Code.HLF1 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='HLF1', tag='HLF1')
TaxRecordPeriod1Code.HLF2 = TaxRecordPeriod1Code._CF_enumeration.addEnumeration(unicode_value='HLF2', tag='HLF2')
TaxRecordPeriod1Code._InitializeFacetMap(TaxRecordPeriod1Code._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaxRecordPeriod1Code', TaxRecordPeriod1Code)
_module_typeBindings.TaxRecordPeriod1Code = TaxRecordPeriod1Code

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TrueFalseIndicator
class TrueFalseIndicator (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrueFalseIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1223, 1)
    _Documentation = None
TrueFalseIndicator._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TrueFalseIndicator', TrueFalseIndicator)
_module_typeBindings.TrueFalseIndicator = TrueFalseIndicator

# Atomic simple type: {urn:CBI:xsd:CBIPaymentRequest.00.04.01}UUIDv4Identifier
class UUIDv4Identifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UUIDv4Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 1226, 1)
    _Documentation = None
UUIDv4Identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
UUIDv4Identifier._CF_pattern.addPattern(pattern='[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}')
UUIDv4Identifier._InitializeFacetMap(UUIDv4Identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UUIDv4Identifier', UUIDv4Identifier)
_module_typeBindings.UUIDv4Identifier = UUIDv4Identifier

# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentRequest.00.04.01 with content type ELEMENT_ONLY
class CBIPaymentRequest_00_04_01 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentRequest.00.04.01 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentRequest.00.04.01')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 7, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GrpHdr uses Python identifier GrpHdr
    __GrpHdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), 'GrpHdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentRequest_00_04_01_urnCBIxsdCBIPaymentRequest_00_04_01GrpHdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 9, 3), )

    
    GrpHdr = property(__GrpHdr.value, __GrpHdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PmtInf uses Python identifier PmtInf
    __PmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtInf'), 'PmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentRequest_00_04_01_urnCBIxsdCBIPaymentRequest_00_04_01PmtInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 13, 3), )

    
    PmtInf = property(__PmtInf.value, __PmtInf.set, None, None)

    _ElementMap.update({
        __GrpHdr.name() : __GrpHdr,
        __PmtInf.name() : __PmtInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentRequest_00_04_01 = CBIPaymentRequest_00_04_01
Namespace.addCategoryObject('typeBinding', 'CBIPaymentRequest.00.04.01', CBIPaymentRequest_00_04_01)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIGroupHeader with content type ELEMENT_ONLY
class CBIGroupHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIGroupHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIGroupHeader')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}MsgId uses Python identifier MsgId
    __MsgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), 'MsgId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_01MsgId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 18, 3), )

    
    MsgId = property(__MsgId.value, __MsgId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreDtTm uses Python identifier CreDtTm
    __CreDtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), 'CreDtTm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_01CreDtTm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 19, 3), )

    
    CreDtTm = property(__CreDtTm.value, __CreDtTm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}NbOfTxs uses Python identifier NbOfTxs
    __NbOfTxs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), 'NbOfTxs', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_01NbOfTxs', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 20, 3), )

    
    NbOfTxs = property(__NbOfTxs.value, __NbOfTxs.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtrlSum uses Python identifier CtrlSum
    __CtrlSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), 'CtrlSum', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_01CtrlSum', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 21, 3), )

    
    CtrlSum = property(__CtrlSum.value, __CtrlSum.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InitgPty uses Python identifier InitgPty
    __InitgPty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InitgPty'), 'InitgPty', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_01InitgPty', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 22, 3), )

    
    InitgPty = property(__InitgPty.value, __InitgPty.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FwdgAgt uses Python identifier FwdgAgt
    __FwdgAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt'), 'FwdgAgt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGroupHeader_urnCBIxsdCBIPaymentRequest_00_04_01FwdgAgt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 23, 3), )

    
    FwdgAgt = property(__FwdgAgt.value, __FwdgAgt.set, None, None)

    _ElementMap.update({
        __MsgId.name() : __MsgId,
        __CreDtTm.name() : __CreDtTm,
        __NbOfTxs.name() : __NbOfTxs,
        __CtrlSum.name() : __CtrlSum,
        __InitgPty.name() : __InitgPty,
        __FwdgAgt.name() : __FwdgAgt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIGroupHeader = CBIGroupHeader
Namespace.addCategoryObject('typeBinding', 'CBIGroupHeader', CBIGroupHeader)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentInstructionInformation with content type ELEMENT_ONLY
class CBIPaymentInstructionInformation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentInstructionInformation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentInstructionInformation')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 33, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PmtInfId uses Python identifier PmtInfId
    __PmtInfId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId'), 'PmtInfId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01PmtInfId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 35, 3), )

    
    PmtInfId = property(__PmtInfId.value, __PmtInfId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PmtMtd uses Python identifier PmtMtd
    __PmtMtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd'), 'PmtMtd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01PmtMtd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 36, 3), )

    
    PmtMtd = property(__PmtMtd.value, __PmtMtd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BtchBookg uses Python identifier BtchBookg
    __BtchBookg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg'), 'BtchBookg', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01BtchBookg', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 37, 3), )

    
    BtchBookg = property(__BtchBookg.value, __BtchBookg.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PmtTpInf uses Python identifier PmtTpInf
    __PmtTpInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), 'PmtTpInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01PmtTpInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 38, 3), )

    
    PmtTpInf = property(__PmtTpInf.value, __PmtTpInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReqdExctnDt uses Python identifier ReqdExctnDt
    __ReqdExctnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt'), 'ReqdExctnDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01ReqdExctnDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 39, 3), )

    
    ReqdExctnDt = property(__ReqdExctnDt.value, __ReqdExctnDt.set, None, ' CHAN: Type Changed into DateAndDateTime2Choice for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dbtr uses Python identifier Dbtr
    __Dbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), 'Dbtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01Dbtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 44, 3), )

    
    Dbtr = property(__Dbtr.value, __Dbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DbtrAcct uses Python identifier DbtrAcct
    __DbtrAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct'), 'DbtrAcct', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01DbtrAcct', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 45, 3), )

    
    DbtrAcct = property(__DbtrAcct.value, __DbtrAcct.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DbtrAgt uses Python identifier DbtrAgt
    __DbtrAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt'), 'DbtrAgt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01DbtrAgt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 46, 3), )

    
    DbtrAgt = property(__DbtrAgt.value, __DbtrAgt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}UltmtDbtr uses Python identifier UltmtDbtr
    __UltmtDbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), 'UltmtDbtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01UltmtDbtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 47, 3), )

    
    UltmtDbtr = property(__UltmtDbtr.value, __UltmtDbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ChrgBr uses Python identifier ChrgBr
    __ChrgBr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr'), 'ChrgBr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01ChrgBr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 48, 3), )

    
    ChrgBr = property(__ChrgBr.value, __ChrgBr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ChrgsAcct uses Python identifier ChrgsAcct
    __ChrgsAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct'), 'ChrgsAcct', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01ChrgsAcct', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 49, 3), )

    
    ChrgsAcct = property(__ChrgsAcct.value, __ChrgsAcct.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtTrfTxInf uses Python identifier CdtTrfTxInf
    __CdtTrfTxInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf'), 'CdtTrfTxInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentInstructionInformation_urnCBIxsdCBIPaymentRequest_00_04_01CdtTrfTxInf', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 50, 3), )

    
    CdtTrfTxInf = property(__CdtTrfTxInf.value, __CdtTrfTxInf.set, None, None)

    _ElementMap.update({
        __PmtInfId.name() : __PmtInfId,
        __PmtMtd.name() : __PmtMtd,
        __BtchBookg.name() : __BtchBookg,
        __PmtTpInf.name() : __PmtTpInf,
        __ReqdExctnDt.name() : __ReqdExctnDt,
        __Dbtr.name() : __Dbtr,
        __DbtrAcct.name() : __DbtrAcct,
        __DbtrAgt.name() : __DbtrAgt,
        __UltmtDbtr.name() : __UltmtDbtr,
        __ChrgBr.name() : __ChrgBr,
        __ChrgsAcct.name() : __ChrgsAcct,
        __CdtTrfTxInf.name() : __CdtTrfTxInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentInstructionInformation = CBIPaymentInstructionInformation
Namespace.addCategoryObject('typeBinding', 'CBIPaymentInstructionInformation', CBIPaymentInstructionInformation)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICreditTransferTransactionInformation with content type ELEMENT_ONLY
class CBICreditTransferTransactionInformation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICreditTransferTransactionInformation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICreditTransferTransactionInformation')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 67, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PmtId uses Python identifier PmtId
    __PmtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtId'), 'PmtId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01PmtId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 69, 3), )

    
    PmtId = property(__PmtId.value, __PmtId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PmtTpInf uses Python identifier PmtTpInf
    __PmtTpInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), 'PmtTpInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01PmtTpInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 70, 3), )

    
    PmtTpInf = property(__PmtTpInf.value, __PmtTpInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 71, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ChqInstr uses Python identifier ChqInstr
    __ChqInstr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChqInstr'), 'ChqInstr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01ChqInstr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 72, 3), )

    
    ChqInstr = property(__ChqInstr.value, __ChqInstr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}UltmtDbtr uses Python identifier UltmtDbtr
    __UltmtDbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), 'UltmtDbtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01UltmtDbtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 73, 3), )

    
    UltmtDbtr = property(__UltmtDbtr.value, __UltmtDbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SrvInf uses Python identifier SrvInf
    __SrvInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SrvInf'), 'SrvInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01SrvInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 74, 3), )

    
    SrvInf = property(__SrvInf.value, __SrvInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtrAgt uses Python identifier CdtrAgt
    __CdtrAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtrAgt'), 'CdtrAgt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01CdtrAgt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 75, 3), )

    
    CdtrAgt = property(__CdtrAgt.value, __CdtrAgt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cdtr uses Python identifier Cdtr
    __Cdtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), 'Cdtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01Cdtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 76, 3), )

    
    Cdtr = property(__Cdtr.value, __Cdtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtrAcct uses Python identifier CdtrAcct
    __CdtrAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtrAcct'), 'CdtrAcct', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01CdtrAcct', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 77, 3), )

    
    CdtrAcct = property(__CdtrAcct.value, __CdtrAcct.set, None, ' CHAN - Type Changed in order to add the optional Proxy Field under Creditor Account ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}UltmtCdtr uses Python identifier UltmtCdtr
    __UltmtCdtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtCdtr'), 'UltmtCdtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01UltmtCdtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 82, 3), )

    
    UltmtCdtr = property(__UltmtCdtr.value, __UltmtCdtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstrForCdtrAgt uses Python identifier InstrForCdtrAgt
    __InstrForCdtrAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrForCdtrAgt'), 'InstrForCdtrAgt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01InstrForCdtrAgt', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 83, 3), )

    
    InstrForCdtrAgt = property(__InstrForCdtrAgt.value, __InstrForCdtrAgt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DestCdtrRsp uses Python identifier DestCdtrRsp
    __DestCdtrRsp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DestCdtrRsp'), 'DestCdtrRsp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01DestCdtrRsp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 84, 3), )

    
    DestCdtrRsp = property(__DestCdtrRsp.value, __DestCdtrRsp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Purp uses Python identifier Purp
    __Purp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Purp'), 'Purp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01Purp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 85, 3), )

    
    Purp = property(__Purp.value, __Purp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RgltryRptg uses Python identifier RgltryRptg
    __RgltryRptg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgltryRptg'), 'RgltryRptg', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01RgltryRptg', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 86, 3), )

    
    RgltryRptg = property(__RgltryRptg.value, __RgltryRptg.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tax uses Python identifier Tax
    __Tax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tax'), 'Tax', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01Tax', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 87, 3), )

    
    Tax = property(__Tax.value, __Tax.set, None, ' CHAN - Complex structure included for the migration to v2019 ISO message ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RltdRmtInf uses Python identifier RltdRmtInf
    __RltdRmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RltdRmtInf'), 'RltdRmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01RltdRmtInf', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 92, 3), )

    
    RltdRmtInf = property(__RltdRmtInf.value, __RltdRmtInf.set, None, ' CHAN - Modified structure to adopt v2019 ISO message ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RmtInf uses Python identifier RmtInf
    __RmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtInf'), 'RmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICreditTransferTransactionInformation_urnCBIxsdCBIPaymentRequest_00_04_01RmtInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 97, 3), )

    
    RmtInf = property(__RmtInf.value, __RmtInf.set, None, None)

    _ElementMap.update({
        __PmtId.name() : __PmtId,
        __PmtTpInf.name() : __PmtTpInf,
        __Amt.name() : __Amt,
        __ChqInstr.name() : __ChqInstr,
        __UltmtDbtr.name() : __UltmtDbtr,
        __SrvInf.name() : __SrvInf,
        __CdtrAgt.name() : __CdtrAgt,
        __Cdtr.name() : __Cdtr,
        __CdtrAcct.name() : __CdtrAcct,
        __UltmtCdtr.name() : __UltmtCdtr,
        __InstrForCdtrAgt.name() : __InstrForCdtrAgt,
        __DestCdtrRsp.name() : __DestCdtrRsp,
        __Purp.name() : __Purp,
        __RgltryRptg.name() : __RgltryRptg,
        __Tax.name() : __Tax,
        __RltdRmtInf.name() : __RltdRmtInf,
        __RmtInf.name() : __RmtInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICreditTransferTransactionInformation = CBICreditTransferTransactionInformation
Namespace.addCategoryObject('typeBinding', 'CBICreditTransferTransactionInformation', CBICreditTransferTransactionInformation)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AddressType3Choice with content type ELEMENT_ONLY
class AddressType3Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AddressType3Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType3Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 119, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_AddressType3Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 121, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_AddressType3Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 122, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressType3Choice = AddressType3Choice
Namespace.addCategoryObject('typeBinding', 'AddressType3Choice', AddressType3Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CategoryPurpose1Choice with content type ELEMENT_ONLY
class CategoryPurpose1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CategoryPurpose1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CategoryPurpose1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 132, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CategoryPurpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 134, 12), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CategoryPurpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 135, 12), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CategoryPurpose1Choice = CategoryPurpose1Choice
Namespace.addCategoryObject('typeBinding', 'CategoryPurpose1Choice', CategoryPurpose1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIAccountIdentification1 with content type ELEMENT_ONLY
class CBIAccountIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIAccountIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIAccountIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 138, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}IBAN uses Python identifier IBAN
    __IBAN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IBAN'), 'IBAN', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIAccountIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01IBAN', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 140, 3), )

    
    IBAN = property(__IBAN.value, __IBAN.set, None, None)

    _ElementMap.update({
        __IBAN.name() : __IBAN
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIAccountIdentification1 = CBIAccountIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIAccountIdentification1', CBIAccountIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIAmountType1 with content type ELEMENT_ONLY
class CBIAmountType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIAmountType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIAmountType1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 143, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstdAmt uses Python identifier InstdAmt
    __InstdAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstdAmt'), 'InstdAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIAmountType1_urnCBIxsdCBIPaymentRequest_00_04_01InstdAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 145, 3), )

    
    InstdAmt = property(__InstdAmt.value, __InstdAmt.set, None, None)

    _ElementMap.update({
        __InstdAmt.name() : __InstdAmt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIAmountType1 = CBIAmountType1
Namespace.addCategoryObject('typeBinding', 'CBIAmountType1', CBIAmountType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIBranchAndFinancialInstitutionIdentification1 with content type ELEMENT_ONLY
class CBIBranchAndFinancialInstitutionIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIBranchAndFinancialInstitutionIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIBranchAndFinancialInstitutionIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 148, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FinInstnId uses Python identifier FinInstnId
    __FinInstnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), 'FinInstnId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIBranchAndFinancialInstitutionIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01FinInstnId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 150, 3), )

    
    FinInstnId = property(__FinInstnId.value, __FinInstnId.set, None, None)

    _ElementMap.update({
        __FinInstnId.name() : __FinInstnId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIBranchAndFinancialInstitutionIdentification1 = CBIBranchAndFinancialInstitutionIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIBranchAndFinancialInstitutionIdentification1', CBIBranchAndFinancialInstitutionIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIBranchAndFinancialInstitutionIdentification2 with content type ELEMENT_ONLY
class CBIBranchAndFinancialInstitutionIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIBranchAndFinancialInstitutionIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIBranchAndFinancialInstitutionIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 153, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FinInstnId uses Python identifier FinInstnId
    __FinInstnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), 'FinInstnId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIBranchAndFinancialInstitutionIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01FinInstnId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 155, 3), )

    
    FinInstnId = property(__FinInstnId.value, __FinInstnId.set, None, None)

    _ElementMap.update({
        __FinInstnId.name() : __FinInstnId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIBranchAndFinancialInstitutionIdentification2 = CBIBranchAndFinancialInstitutionIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIBranchAndFinancialInstitutionIdentification2', CBIBranchAndFinancialInstitutionIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIBranchAndFinancialInstitutionIdentification3 with content type ELEMENT_ONLY
class CBIBranchAndFinancialInstitutionIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIBranchAndFinancialInstitutionIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIBranchAndFinancialInstitutionIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 158, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FinInstnId uses Python identifier FinInstnId
    __FinInstnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), 'FinInstnId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIBranchAndFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01FinInstnId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 160, 3), )

    
    FinInstnId = property(__FinInstnId.value, __FinInstnId.set, None, None)

    _ElementMap.update({
        __FinInstnId.name() : __FinInstnId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIBranchAndFinancialInstitutionIdentification3 = CBIBranchAndFinancialInstitutionIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIBranchAndFinancialInstitutionIdentification3', CBIBranchAndFinancialInstitutionIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICashAccount1 with content type ELEMENT_ONLY
class CBICashAccount1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICashAccount1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICashAccount1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 163, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICashAccount1_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 165, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICashAccount1 = CBICashAccount1
Namespace.addCategoryObject('typeBinding', 'CBICashAccount1', CBICashAccount1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICashAccount2 with content type ELEMENT_ONLY
class CBICashAccount2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICashAccount2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICashAccount2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 168, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICashAccount2_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 170, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICashAccount2_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 171, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Tp.name() : __Tp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICashAccount2 = CBICashAccount2
Namespace.addCategoryObject('typeBinding', 'CBICashAccount2', CBICashAccount2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICashAccount3 with content type ELEMENT_ONLY
class CBICashAccount3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICashAccount3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICashAccount3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 174, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICashAccount3_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 176, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICashAccount3 = CBICashAccount3
Namespace.addCategoryObject('typeBinding', 'CBICashAccount3', CBICashAccount3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CashAccountType2Choice with content type ELEMENT_ONLY
class CashAccountType2Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CashAccountType2Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CashAccountType2Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 179, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CashAccountType2Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 181, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CashAccountType2Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 182, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CashAccountType2Choice = CashAccountType2Choice
Namespace.addCategoryObject('typeBinding', 'CashAccountType2Choice', CashAccountType2Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICheque1 with content type ELEMENT_ONLY
class CBICheque1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBICheque1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBICheque1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 185, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ChqTp uses Python identifier ChqTp
    __ChqTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChqTp'), 'ChqTp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBICheque1_urnCBIxsdCBIPaymentRequest_00_04_01ChqTp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 187, 3), )

    
    ChqTp = property(__ChqTp.value, __ChqTp.set, None, None)

    _ElementMap.update({
        __ChqTp.name() : __ChqTp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBICheque1 = CBICheque1
Namespace.addCategoryObject('typeBinding', 'CBICheque1', CBICheque1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIClearingSystemMemberIdentification1 with content type ELEMENT_ONLY
class CBIClearingSystemMemberIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIClearingSystemMemberIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIClearingSystemMemberIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 190, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}MmbId uses Python identifier MmbId
    __MmbId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MmbId'), 'MmbId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIClearingSystemMemberIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01MmbId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 192, 3), )

    
    MmbId = property(__MmbId.value, __MmbId.set, None, None)

    _ElementMap.update({
        __MmbId.name() : __MmbId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIClearingSystemMemberIdentification1 = CBIClearingSystemMemberIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIClearingSystemMemberIdentification1', CBIClearingSystemMemberIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIFinancialInstitutionIdentification1 with content type ELEMENT_ONLY
class CBIFinancialInstitutionIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIFinancialInstitutionIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIFinancialInstitutionIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 195, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ClrSysMmbId uses Python identifier ClrSysMmbId
    __ClrSysMmbId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), 'ClrSysMmbId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIFinancialInstitutionIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01ClrSysMmbId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 197, 3), )

    
    ClrSysMmbId = property(__ClrSysMmbId.value, __ClrSysMmbId.set, None, None)

    _ElementMap.update({
        __ClrSysMmbId.name() : __ClrSysMmbId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIFinancialInstitutionIdentification1 = CBIFinancialInstitutionIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIFinancialInstitutionIdentification1', CBIFinancialInstitutionIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIFinancialInstitutionIdentification2 with content type ELEMENT_ONLY
class CBIFinancialInstitutionIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIFinancialInstitutionIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIFinancialInstitutionIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 200, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BICFI uses Python identifier BICFI
    __BICFI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BICFI'), 'BICFI', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIFinancialInstitutionIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01BICFI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 202, 3), )

    
    BICFI = property(__BICFI.value, __BICFI.set, None, ' CHAN: Name Changed into BICFI and Type Changed into BICFIDec2014Identifier for v2019 ISO message migration ')

    _ElementMap.update({
        __BICFI.name() : __BICFI
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIFinancialInstitutionIdentification2 = CBIFinancialInstitutionIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIFinancialInstitutionIdentification2', CBIFinancialInstitutionIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIFinancialInstitutionIdentification3 with content type ELEMENT_ONLY
class CBIFinancialInstitutionIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIFinancialInstitutionIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIFinancialInstitutionIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 209, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BICFI uses Python identifier BICFI
    __BICFI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BICFI'), 'BICFI', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01BICFI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 211, 3), )

    
    BICFI = property(__BICFI.value, __BICFI.set, None, ' CHAN: Name Changed into BICFI and Type Changed into BICFIDec2014Identifier for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ClrSysMmbId uses Python identifier ClrSysMmbId
    __ClrSysMmbId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), 'ClrSysMmbId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01ClrSysMmbId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 216, 3), )

    
    ClrSysMmbId = property(__ClrSysMmbId.value, __ClrSysMmbId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIFinancialInstitutionIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01LEI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 217, 3), )

    
    LEI = property(__LEI.value, __LEI.set, None, ' CHAN: Field included for v2019 ISO message migration ')

    _ElementMap.update({
        __BICFI.name() : __BICFI,
        __ClrSysMmbId.name() : __ClrSysMmbId,
        __LEI.name() : __LEI
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIFinancialInstitutionIdentification3 = CBIFinancialInstitutionIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIFinancialInstitutionIdentification3', CBIFinancialInstitutionIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIGenericIdentification1 with content type ELEMENT_ONLY
class CBIGenericIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIGenericIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIGenericIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 224, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGenericIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 226, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGenericIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 227, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIGenericIdentification1 = CBIGenericIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIGenericIdentification1', CBIGenericIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIGenericIdentification2 with content type ELEMENT_ONLY
class CBIGenericIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIGenericIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIGenericIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 230, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGenericIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 232, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIGenericIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 233, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIGenericIdentification2 = CBIGenericIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIGenericIdentification2', CBIGenericIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIIdType1 with content type ELEMENT_ONLY
class CBIIdType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIIdType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIIdType1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 236, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIIdType1_urnCBIxsdCBIPaymentRequest_00_04_01OrgId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 238, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIIdType1 = CBIIdType1
Namespace.addCategoryObject('typeBinding', 'CBIIdType1', CBIIdType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIIdType2 with content type ELEMENT_ONLY
class CBIIdType2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIIdType2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIIdType2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 241, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIIdType2_urnCBIxsdCBIPaymentRequest_00_04_01OrgId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 243, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, ' CHAN: Removed "OR" XSD check and restored "sequence" for ISO 20022 compliance ')

    _ElementMap.update({
        __OrgId.name() : __OrgId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIIdType2 = CBIIdType2
Namespace.addCategoryObject('typeBinding', 'CBIIdType2', CBIIdType2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIIdType3 with content type ELEMENT_ONLY
class CBIIdType3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIIdType3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIIdType3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 250, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIIdType3_urnCBIxsdCBIPaymentRequest_00_04_01OrgId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 252, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIIdType3 = CBIIdType3
Namespace.addCategoryObject('typeBinding', 'CBIIdType3', CBIIdType3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBILocalInstrument1 with content type ELEMENT_ONLY
class CBILocalInstrument1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBILocalInstrument1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBILocalInstrument1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 255, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBILocalInstrument1_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 257, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBILocalInstrument1 = CBILocalInstrument1
Namespace.addCategoryObject('typeBinding', 'CBILocalInstrument1', CBILocalInstrument1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBILocalInstrument2 with content type ELEMENT_ONLY
class CBILocalInstrument2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBILocalInstrument2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBILocalInstrument2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 260, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBILocalInstrument2_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 262, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBILocalInstrument2 = CBILocalInstrument2
Namespace.addCategoryObject('typeBinding', 'CBILocalInstrument2', CBILocalInstrument2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification1 with content type ELEMENT_ONLY
class CBIOrganisationIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 265, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Othr', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 267, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification1 = CBIOrganisationIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification1', CBIOrganisationIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification2 with content type ELEMENT_ONLY
class CBIOrganisationIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 270, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AnyBIC uses Python identifier AnyBIC
    __AnyBIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), 'AnyBIC', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01AnyBIC', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 272, 3), )

    
    AnyBIC = property(__AnyBIC.value, __AnyBIC.set, None, ' CHAN: Name Changed into AnyBIC and Type Changed into AnyBICDec2014Identifier for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01LEI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 277, 3), )

    
    LEI = property(__LEI.value, __LEI.set, None, ' CHAN: Field included for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01Othr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 282, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __AnyBIC.name() : __AnyBIC,
        __LEI.name() : __LEI,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification2 = CBIOrganisationIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification2', CBIOrganisationIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification3 with content type ELEMENT_ONLY
class CBIOrganisationIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 285, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AnyBIC uses Python identifier AnyBIC
    __AnyBIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), 'AnyBIC', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01AnyBIC', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 287, 3), )

    
    AnyBIC = property(__AnyBIC.value, __AnyBIC.set, None, ' CHAN: Name Changed into AnyBIC and Type Changed into AnyBICDec2014Identifier for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01LEI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 292, 3), )

    
    LEI = property(__LEI.value, __LEI.set, None, ' CHAN: Field included for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01Othr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 297, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __AnyBIC.name() : __AnyBIC,
        __LEI.name() : __LEI,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification3 = CBIOrganisationIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification3', CBIOrganisationIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification4 with content type ELEMENT_ONLY
class CBIOrganisationIdentification4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIOrganisationIdentification4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIOrganisationIdentification4')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 300, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIOrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01Othr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 302, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIOrganisationIdentification4 = CBIOrganisationIdentification4
Namespace.addCategoryObject('typeBinding', 'CBIOrganisationIdentification4', CBIOrganisationIdentification4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIParty1Choice with content type ELEMENT_ONLY
class CBIParty1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIParty1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIParty1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 305, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIParty1Choice_urnCBIxsdCBIPaymentRequest_00_04_01OrgId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 307, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, ' CHAN: Removed "OR" XSD check and restored "sequence" for ISO 20022 compliance ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PrvtId uses Python identifier PrvtId
    __PrvtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), 'PrvtId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIParty1Choice_urnCBIxsdCBIPaymentRequest_00_04_01PrvtId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 312, 3), )

    
    PrvtId = property(__PrvtId.value, __PrvtId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId,
        __PrvtId.name() : __PrvtId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIParty1Choice = CBIParty1Choice
Namespace.addCategoryObject('typeBinding', 'CBIParty1Choice', CBIParty1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification1 with content type ELEMENT_ONLY
class CBIPartyIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 315, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 317, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 318, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification1 = CBIPartyIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification1', CBIPartyIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification2 with content type ELEMENT_ONLY
class CBIPartyIdentification2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 321, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 323, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01PstlAdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 324, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, ' CHAN: Type Changed into CBIPostalAddress24 for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 329, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification2_urnCBIxsdCBIPaymentRequest_00_04_01CtryOfRes', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 330, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification2 = CBIPartyIdentification2
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification2', CBIPartyIdentification2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification3 with content type ELEMENT_ONLY
class CBIPartyIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 333, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 335, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01PstlAdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 336, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, ' CHAN: Type Changed into CBIPostalAddress24 for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 341, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01CtryOfRes', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 342, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification3 = CBIPartyIdentification3
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification3', CBIPartyIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification4 with content type ELEMENT_ONLY
class CBIPartyIdentification4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification4')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 345, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 347, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01PstlAdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 348, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, ' CHAN: Type Changed into CBIPostalAddress24 for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 353, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01CtryOfRes', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 354, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification4 = CBIPartyIdentification4
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification4', CBIPartyIdentification4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification5 with content type ELEMENT_ONLY
class CBIPartyIdentification5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPartyIdentification5 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPartyIdentification5')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 357, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification5_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 359, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPartyIdentification5_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 360, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPartyIdentification5 = CBIPartyIdentification5
Namespace.addCategoryObject('typeBinding', 'CBIPartyIdentification5', CBIPartyIdentification5)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentTypeInformation1 with content type ELEMENT_ONLY
class CBIPaymentTypeInformation1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentTypeInformation1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentTypeInformation1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 363, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstrPrty uses Python identifier InstrPrty
    __InstrPrty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrPrty'), 'InstrPrty', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentTypeInformation1_urnCBIxsdCBIPaymentRequest_00_04_01InstrPrty', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 365, 3), )

    
    InstrPrty = property(__InstrPrty.value, __InstrPrty.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SvcLvl uses Python identifier SvcLvl
    __SvcLvl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), 'SvcLvl', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentTypeInformation1_urnCBIxsdCBIPaymentRequest_00_04_01SvcLvl', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 366, 3), )

    
    SvcLvl = property(__SvcLvl.value, __SvcLvl.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LclInstrm uses Python identifier LclInstrm
    __LclInstrm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm'), 'LclInstrm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentTypeInformation1_urnCBIxsdCBIPaymentRequest_00_04_01LclInstrm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 367, 3), )

    
    LclInstrm = property(__LclInstrm.value, __LclInstrm.set, None, None)

    _ElementMap.update({
        __InstrPrty.name() : __InstrPrty,
        __SvcLvl.name() : __SvcLvl,
        __LclInstrm.name() : __LclInstrm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentTypeInformation1 = CBIPaymentTypeInformation1
Namespace.addCategoryObject('typeBinding', 'CBIPaymentTypeInformation1', CBIPaymentTypeInformation1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentTypeInformation2 with content type ELEMENT_ONLY
class CBIPaymentTypeInformation2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPaymentTypeInformation2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentTypeInformation2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 370, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SvcLvl uses Python identifier SvcLvl
    __SvcLvl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), 'SvcLvl', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentTypeInformation2_urnCBIxsdCBIPaymentRequest_00_04_01SvcLvl', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 372, 3), )

    
    SvcLvl = property(__SvcLvl.value, __SvcLvl.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LclInstrm uses Python identifier LclInstrm
    __LclInstrm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm'), 'LclInstrm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentTypeInformation2_urnCBIxsdCBIPaymentRequest_00_04_01LclInstrm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 373, 3), )

    
    LclInstrm = property(__LclInstrm.value, __LclInstrm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtgyPurp uses Python identifier CtgyPurp
    __CtgyPurp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtgyPurp'), 'CtgyPurp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPaymentTypeInformation2_urnCBIxsdCBIPaymentRequest_00_04_01CtgyPurp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 374, 3), )

    
    CtgyPurp = property(__CtgyPurp.value, __CtgyPurp.set, None, None)

    _ElementMap.update({
        __SvcLvl.name() : __SvcLvl,
        __LclInstrm.name() : __LclInstrm,
        __CtgyPurp.name() : __CtgyPurp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPaymentTypeInformation2 = CBIPaymentTypeInformation2
Namespace.addCategoryObject('typeBinding', 'CBIPaymentTypeInformation2', CBIPaymentTypeInformation2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPersonIdentification1 with content type ELEMENT_ONLY
class CBIPersonIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPersonIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPersonIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 377, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Othr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 379, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPersonIdentification1 = CBIPersonIdentification1
Namespace.addCategoryObject('typeBinding', 'CBIPersonIdentification1', CBIPersonIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPostalAddress24 with content type ELEMENT_ONLY
class CBIPostalAddress24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIPostalAddress24 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIPostalAddress24')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 382, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdrTp uses Python identifier AdrTp
    __AdrTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdrTp'), 'AdrTp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01AdrTp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 384, 3), )

    
    AdrTp = property(__AdrTp.value, __AdrTp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dept uses Python identifier Dept
    __Dept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dept'), 'Dept', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Dept', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 385, 3), )

    
    Dept = property(__Dept.value, __Dept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SubDept uses Python identifier SubDept
    __SubDept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubDept'), 'SubDept', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01SubDept', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 386, 3), )

    
    SubDept = property(__SubDept.value, __SubDept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}StrtNm uses Python identifier StrtNm
    __StrtNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), 'StrtNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01StrtNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 387, 3), )

    
    StrtNm = property(__StrtNm.value, __StrtNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BldgNb uses Python identifier BldgNb
    __BldgNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BldgNb'), 'BldgNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01BldgNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 388, 3), )

    
    BldgNb = property(__BldgNb.value, __BldgNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BldgNm uses Python identifier BldgNm
    __BldgNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BldgNm'), 'BldgNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01BldgNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 389, 3), )

    
    BldgNm = property(__BldgNm.value, __BldgNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Flr uses Python identifier Flr
    __Flr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Flr'), 'Flr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Flr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 390, 3), )

    
    Flr = property(__Flr.value, __Flr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstBx uses Python identifier PstBx
    __PstBx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstBx'), 'PstBx', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01PstBx', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 391, 3), )

    
    PstBx = property(__PstBx.value, __PstBx.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Room uses Python identifier Room
    __Room = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Room'), 'Room', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Room', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 392, 3), )

    
    Room = property(__Room.value, __Room.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstCd uses Python identifier PstCd
    __PstCd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstCd'), 'PstCd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01PstCd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 393, 3), )

    
    PstCd = property(__PstCd.value, __PstCd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TwnNm uses Python identifier TwnNm
    __TwnNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), 'TwnNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01TwnNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 394, 3), )

    
    TwnNm = property(__TwnNm.value, __TwnNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TwnLctnNm uses Python identifier TwnLctnNm
    __TwnLctnNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TwnLctnNm'), 'TwnLctnNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01TwnLctnNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 395, 3), )

    
    TwnLctnNm = property(__TwnLctnNm.value, __TwnLctnNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DstrctNm uses Python identifier DstrctNm
    __DstrctNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm'), 'DstrctNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01DstrctNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 396, 3), )

    
    DstrctNm = property(__DstrctNm.value, __DstrctNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtrySubDvsn uses Python identifier CtrySubDvsn
    __CtrySubDvsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn'), 'CtrySubDvsn', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01CtrySubDvsn', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 397, 3), )

    
    CtrySubDvsn = property(__CtrySubDvsn.value, __CtrySubDvsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Ctry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 398, 3), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdrLine uses Python identifier AdrLine
    __AdrLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdrLine'), 'AdrLine', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIPostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01AdrLine', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 399, 3), )

    
    AdrLine = property(__AdrLine.value, __AdrLine.set, None, None)

    _ElementMap.update({
        __AdrTp.name() : __AdrTp,
        __Dept.name() : __Dept,
        __SubDept.name() : __SubDept,
        __StrtNm.name() : __StrtNm,
        __BldgNb.name() : __BldgNb,
        __BldgNm.name() : __BldgNm,
        __Flr.name() : __Flr,
        __PstBx.name() : __PstBx,
        __Room.name() : __Room,
        __PstCd.name() : __PstCd,
        __TwnNm.name() : __TwnNm,
        __TwnLctnNm.name() : __TwnLctnNm,
        __DstrctNm.name() : __DstrctNm,
        __CtrySubDvsn.name() : __CtrySubDvsn,
        __Ctry.name() : __Ctry,
        __AdrLine.name() : __AdrLine
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIPostalAddress24 = CBIPostalAddress24
Namespace.addCategoryObject('typeBinding', 'CBIPostalAddress24', CBIPostalAddress24)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRegulatoryReporting1 with content type ELEMENT_ONLY
class CBIRegulatoryReporting1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRegulatoryReporting1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRegulatoryReporting1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 402, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DbtCdtRptgInd uses Python identifier DbtCdtRptgInd
    __DbtCdtRptgInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtCdtRptgInd'), 'DbtCdtRptgInd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_01DbtCdtRptgInd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 404, 3), )

    
    DbtCdtRptgInd = property(__DbtCdtRptgInd.value, __DbtCdtRptgInd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dtls uses Python identifier Dtls
    __Dtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dtls'), 'Dtls', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_01Dtls', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 405, 3), )

    
    Dtls = property(__Dtls.value, __Dtls.set, None, None)

    _ElementMap.update({
        __DbtCdtRptgInd.name() : __DbtCdtRptgInd,
        __Dtls.name() : __Dtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIRegulatoryReporting1 = CBIRegulatoryReporting1
Namespace.addCategoryObject('typeBinding', 'CBIRegulatoryReporting1', CBIRegulatoryReporting1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRemittanceLocation1 with content type ELEMENT_ONLY
class CBIRemittanceLocation1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRemittanceLocation1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRemittanceLocation1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 408, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RmtId uses Python identifier RmtId
    __RmtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtId'), 'RmtId', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIRemittanceLocation1_urnCBIxsdCBIPaymentRequest_00_04_01RmtId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 410, 3), )

    
    RmtId = property(__RmtId.value, __RmtId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RmtLctnDtls uses Python identifier RmtLctnDtls
    __RmtLctnDtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnDtls'), 'RmtLctnDtls', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIRemittanceLocation1_urnCBIxsdCBIPaymentRequest_00_04_01RmtLctnDtls', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 411, 3), )

    
    RmtLctnDtls = property(__RmtLctnDtls.value, __RmtLctnDtls.set, None, ' CHAN: Element included for v2019 ISO message migration ')

    _ElementMap.update({
        __RmtId.name() : __RmtId,
        __RmtLctnDtls.name() : __RmtLctnDtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIRemittanceLocation1 = CBIRemittanceLocation1
Namespace.addCategoryObject('typeBinding', 'CBIRemittanceLocation1', CBIRemittanceLocation1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRemittanceLocationData1 with content type ELEMENT_ONLY
class CBIRemittanceLocationData1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIRemittanceLocationData1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIRemittanceLocationData1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 418, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Mtd uses Python identifier Mtd
    __Mtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mtd'), 'Mtd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIRemittanceLocationData1_urnCBIxsdCBIPaymentRequest_00_04_01Mtd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 420, 3), )

    
    Mtd = property(__Mtd.value, __Mtd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ElctrncAdr uses Python identifier ElctrncAdr
    __ElctrncAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ElctrncAdr'), 'ElctrncAdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIRemittanceLocationData1_urnCBIxsdCBIPaymentRequest_00_04_01ElctrncAdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 421, 3), )

    
    ElctrncAdr = property(__ElctrncAdr.value, __ElctrncAdr.set, None, None)

    _ElementMap.update({
        __Mtd.name() : __Mtd,
        __ElctrncAdr.name() : __ElctrncAdr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIRemittanceLocationData1 = CBIRemittanceLocationData1
Namespace.addCategoryObject('typeBinding', 'CBIRemittanceLocationData1', CBIRemittanceLocationData1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIServiceLevel1 with content type ELEMENT_ONLY
class CBIServiceLevel1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIServiceLevel1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIServiceLevel1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 424, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIServiceLevel1_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 426, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIServiceLevel1 = CBIServiceLevel1
Namespace.addCategoryObject('typeBinding', 'CBIServiceLevel1', CBIServiceLevel1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIServiceLevel2 with content type ELEMENT_ONLY
class CBIServiceLevel2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIServiceLevel2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIServiceLevel2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 429, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIServiceLevel2_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 431, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIServiceLevel2 = CBIServiceLevel2
Namespace.addCategoryObject('typeBinding', 'CBIServiceLevel2', CBIServiceLevel2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIStructuredRegulatoryReporting1 with content type ELEMENT_ONLY
class CBIStructuredRegulatoryReporting1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CBIStructuredRegulatoryReporting1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CBIStructuredRegulatoryReporting1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 434, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIStructuredRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 436, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIStructuredRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 445, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Inf uses Python identifier Inf
    __Inf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Inf'), 'Inf', '__urnCBIxsdCBIPaymentRequest_00_04_01_CBIStructuredRegulatoryReporting1_urnCBIxsdCBIPaymentRequest_00_04_01Inf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 446, 3), )

    
    Inf = property(__Inf.value, __Inf.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Amt.name() : __Amt,
        __Inf.name() : __Inf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CBIStructuredRegulatoryReporting1 = CBIStructuredRegulatoryReporting1
Namespace.addCategoryObject('typeBinding', 'CBIStructuredRegulatoryReporting1', CBIStructuredRegulatoryReporting1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditorReferenceInformation2 with content type ELEMENT_ONLY
class CreditorReferenceInformation2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditorReferenceInformation2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditorReferenceInformation2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 449, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_CreditorReferenceInformation2_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 451, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Ref uses Python identifier Ref
    __Ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ref'), 'Ref', '__urnCBIxsdCBIPaymentRequest_00_04_01_CreditorReferenceInformation2_urnCBIxsdCBIPaymentRequest_00_04_01Ref', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 452, 3), )

    
    Ref = property(__Ref.value, __Ref.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Ref.name() : __Ref
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditorReferenceInformation2 = CreditorReferenceInformation2
Namespace.addCategoryObject('typeBinding', 'CreditorReferenceInformation2', CreditorReferenceInformation2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditorReferenceType1Choice with content type ELEMENT_ONLY
class CreditorReferenceType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditorReferenceType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditorReferenceType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 455, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_CreditorReferenceType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 458, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CreditorReferenceType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 459, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditorReferenceType1Choice = CreditorReferenceType1Choice
Namespace.addCategoryObject('typeBinding', 'CreditorReferenceType1Choice', CreditorReferenceType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditorReferenceType2 with content type ELEMENT_ONLY
class CreditorReferenceType2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CreditorReferenceType2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreditorReferenceType2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 463, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdOrPrtry uses Python identifier CdOrPrtry
    __CdOrPrtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), 'CdOrPrtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_CreditorReferenceType2_urnCBIxsdCBIPaymentRequest_00_04_01CdOrPrtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 465, 3), )

    
    CdOrPrtry = property(__CdOrPrtry.value, __CdOrPrtry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_CreditorReferenceType2_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 466, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __CdOrPrtry.name() : __CdOrPrtry,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CreditorReferenceType2 = CreditorReferenceType2
Namespace.addCategoryObject('typeBinding', 'CreditorReferenceType2', CreditorReferenceType2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DateAndPlaceOfBirth1 with content type ELEMENT_ONLY
class DateAndPlaceOfBirth1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DateAndPlaceOfBirth1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateAndPlaceOfBirth1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 469, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BirthDt uses Python identifier BirthDt
    __BirthDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BirthDt'), 'BirthDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DateAndPlaceOfBirth1_urnCBIxsdCBIPaymentRequest_00_04_01BirthDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 471, 3), )

    
    BirthDt = property(__BirthDt.value, __BirthDt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PrvcOfBirth uses Python identifier PrvcOfBirth
    __PrvcOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth'), 'PrvcOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_01_DateAndPlaceOfBirth1_urnCBIxsdCBIPaymentRequest_00_04_01PrvcOfBirth', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 472, 3), )

    
    PrvcOfBirth = property(__PrvcOfBirth.value, __PrvcOfBirth.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CityOfBirth uses Python identifier CityOfBirth
    __CityOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth'), 'CityOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_01_DateAndPlaceOfBirth1_urnCBIxsdCBIPaymentRequest_00_04_01CityOfBirth', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 473, 3), )

    
    CityOfBirth = property(__CityOfBirth.value, __CityOfBirth.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtryOfBirth uses Python identifier CtryOfBirth
    __CtryOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth'), 'CtryOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_01_DateAndPlaceOfBirth1_urnCBIxsdCBIPaymentRequest_00_04_01CtryOfBirth', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 474, 3), )

    
    CtryOfBirth = property(__CtryOfBirth.value, __CtryOfBirth.set, None, None)

    _ElementMap.update({
        __BirthDt.name() : __BirthDt,
        __PrvcOfBirth.name() : __PrvcOfBirth,
        __CityOfBirth.name() : __CityOfBirth,
        __CtryOfBirth.name() : __CtryOfBirth
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateAndPlaceOfBirth1 = DateAndPlaceOfBirth1
Namespace.addCategoryObject('typeBinding', 'DateAndPlaceOfBirth1', DateAndPlaceOfBirth1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DateAndDateTime2Choice with content type ELEMENT_ONLY
class DateAndDateTime2Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DateAndDateTime2Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateAndDateTime2Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 477, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dt uses Python identifier Dt
    __Dt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dt'), 'Dt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DateAndDateTime2Choice_urnCBIxsdCBIPaymentRequest_00_04_01Dt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 479, 3), )

    
    Dt = property(__Dt.value, __Dt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DtTm uses Python identifier DtTm
    __DtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DtTm'), 'DtTm', '__urnCBIxsdCBIPaymentRequest_00_04_01_DateAndDateTime2Choice_urnCBIxsdCBIPaymentRequest_00_04_01DtTm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 480, 3), )

    
    DtTm = property(__DtTm.value, __DtTm.set, None, None)

    _ElementMap.update({
        __Dt.name() : __Dt,
        __DtTm.name() : __DtTm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateAndDateTime2Choice = DateAndDateTime2Choice
Namespace.addCategoryObject('typeBinding', 'DateAndDateTime2Choice', DateAndDateTime2Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DatePeriod2 with content type ELEMENT_ONLY
class DatePeriod2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DatePeriod2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatePeriod2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 483, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FrDt uses Python identifier FrDt
    __FrDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrDt'), 'FrDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DatePeriod2_urnCBIxsdCBIPaymentRequest_00_04_01FrDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 485, 3), )

    
    FrDt = property(__FrDt.value, __FrDt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ToDt uses Python identifier ToDt
    __ToDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ToDt'), 'ToDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DatePeriod2_urnCBIxsdCBIPaymentRequest_00_04_01ToDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 486, 3), )

    
    ToDt = property(__ToDt.value, __ToDt.set, None, None)

    _ElementMap.update({
        __FrDt.name() : __FrDt,
        __ToDt.name() : __ToDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DatePeriod2 = DatePeriod2
Namespace.addCategoryObject('typeBinding', 'DatePeriod2', DatePeriod2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DiscountAmountAndType1 with content type ELEMENT_ONLY
class DiscountAmountAndType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DiscountAmountAndType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DiscountAmountAndType1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 489, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_DiscountAmountAndType1_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 491, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DiscountAmountAndType1_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 492, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Amt.name() : __Amt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DiscountAmountAndType1 = DiscountAmountAndType1
Namespace.addCategoryObject('typeBinding', 'DiscountAmountAndType1', DiscountAmountAndType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DiscountAmountType1Choice with content type ELEMENT_ONLY
class DiscountAmountType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DiscountAmountType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DiscountAmountType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 495, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_DiscountAmountType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 497, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_DiscountAmountType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 498, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DiscountAmountType1Choice = DiscountAmountType1Choice
Namespace.addCategoryObject('typeBinding', 'DiscountAmountType1Choice', DiscountAmountType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentAdjustment1 with content type ELEMENT_ONLY
class DocumentAdjustment1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentAdjustment1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentAdjustment1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 501, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 503, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtDbtInd uses Python identifier CdtDbtInd
    __CdtDbtInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtDbtInd'), 'CdtDbtInd', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_01CdtDbtInd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 504, 3), )

    
    CdtDbtInd = property(__CdtDbtInd.value, __CdtDbtInd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Rsn uses Python identifier Rsn
    __Rsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rsn'), 'Rsn', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_01Rsn', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 505, 3), )

    
    Rsn = property(__Rsn.value, __Rsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AddtlInf uses Python identifier AddtlInf
    __AddtlInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf'), 'AddtlInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentAdjustment1_urnCBIxsdCBIPaymentRequest_00_04_01AddtlInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 506, 3), )

    
    AddtlInf = property(__AddtlInf.value, __AddtlInf.set, None, None)

    _ElementMap.update({
        __Amt.name() : __Amt,
        __CdtDbtInd.name() : __CdtDbtInd,
        __Rsn.name() : __Rsn,
        __AddtlInf.name() : __AddtlInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentAdjustment1 = DocumentAdjustment1
Namespace.addCategoryObject('typeBinding', 'DocumentAdjustment1', DocumentAdjustment1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineIdentification1 with content type ELEMENT_ONLY
class DocumentLineIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentLineIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 509, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 511, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nb uses Python identifier Nb
    __Nb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nb'), 'Nb', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Nb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 512, 3), )

    
    Nb = property(__Nb.value, __Nb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RltdDt uses Python identifier RltdDt
    __RltdDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RltdDt'), 'RltdDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01RltdDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 513, 3), )

    
    RltdDt = property(__RltdDt.value, __RltdDt.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Nb.name() : __Nb,
        __RltdDt.name() : __RltdDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentLineIdentification1 = DocumentLineIdentification1
Namespace.addCategoryObject('typeBinding', 'DocumentLineIdentification1', DocumentLineIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineInformation1 with content type ELEMENT_ONLY
class DocumentLineInformation1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineInformation1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentLineInformation1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 516, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineInformation1_urnCBIxsdCBIPaymentRequest_00_04_01Id', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 518, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Desc uses Python identifier Desc
    __Desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Desc'), 'Desc', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineInformation1_urnCBIxsdCBIPaymentRequest_00_04_01Desc', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 519, 3), )

    
    Desc = property(__Desc.value, __Desc.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineInformation1_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 520, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Desc.name() : __Desc,
        __Amt.name() : __Amt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentLineInformation1 = DocumentLineInformation1
Namespace.addCategoryObject('typeBinding', 'DocumentLineInformation1', DocumentLineInformation1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineType1 with content type ELEMENT_ONLY
class DocumentLineType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentLineType1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 523, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdOrPrtry uses Python identifier CdOrPrtry
    __CdOrPrtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), 'CdOrPrtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineType1_urnCBIxsdCBIPaymentRequest_00_04_01CdOrPrtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 525, 3), )

    
    CdOrPrtry = property(__CdOrPrtry.value, __CdOrPrtry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineType1_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 526, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __CdOrPrtry.name() : __CdOrPrtry,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentLineType1 = DocumentLineType1
Namespace.addCategoryObject('typeBinding', 'DocumentLineType1', DocumentLineType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineType1Choice with content type ELEMENT_ONLY
class DocumentLineType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DocumentLineType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DocumentLineType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 529, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 531, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_DocumentLineType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 532, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DocumentLineType1Choice = DocumentLineType1Choice
Namespace.addCategoryObject('typeBinding', 'DocumentLineType1Choice', DocumentLineType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Garnishment3 with content type ELEMENT_ONLY
class Garnishment3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Garnishment3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Garnishment3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 535, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 537, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Grnshee uses Python identifier Grnshee
    __Grnshee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Grnshee'), 'Grnshee', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01Grnshee', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 538, 3), )

    
    Grnshee = property(__Grnshee.value, __Grnshee.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GrnshmtAdmstr uses Python identifier GrnshmtAdmstr
    __GrnshmtAdmstr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GrnshmtAdmstr'), 'GrnshmtAdmstr', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01GrnshmtAdmstr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 539, 3), )

    
    GrnshmtAdmstr = property(__GrnshmtAdmstr.value, __GrnshmtAdmstr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RefNb uses Python identifier RefNb
    __RefNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RefNb'), 'RefNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01RefNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 540, 3), )

    
    RefNb = property(__RefNb.value, __RefNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dt uses Python identifier Dt
    __Dt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dt'), 'Dt', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01Dt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 541, 3), )

    
    Dt = property(__Dt.value, __Dt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RmtdAmt uses Python identifier RmtdAmt
    __RmtdAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), 'RmtdAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01RmtdAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 542, 3), )

    
    RmtdAmt = property(__RmtdAmt.value, __RmtdAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FmlyMdclInsrncInd uses Python identifier FmlyMdclInsrncInd
    __FmlyMdclInsrncInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FmlyMdclInsrncInd'), 'FmlyMdclInsrncInd', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01FmlyMdclInsrncInd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 543, 3), )

    
    FmlyMdclInsrncInd = property(__FmlyMdclInsrncInd.value, __FmlyMdclInsrncInd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}MplyeeTermntnInd uses Python identifier MplyeeTermntnInd
    __MplyeeTermntnInd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MplyeeTermntnInd'), 'MplyeeTermntnInd', '__urnCBIxsdCBIPaymentRequest_00_04_01_Garnishment3_urnCBIxsdCBIPaymentRequest_00_04_01MplyeeTermntnInd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 544, 3), )

    
    MplyeeTermntnInd = property(__MplyeeTermntnInd.value, __MplyeeTermntnInd.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Grnshee.name() : __Grnshee,
        __GrnshmtAdmstr.name() : __GrnshmtAdmstr,
        __RefNb.name() : __RefNb,
        __Dt.name() : __Dt,
        __RmtdAmt.name() : __RmtdAmt,
        __FmlyMdclInsrncInd.name() : __FmlyMdclInsrncInd,
        __MplyeeTermntnInd.name() : __MplyeeTermntnInd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Garnishment3 = Garnishment3
Namespace.addCategoryObject('typeBinding', 'Garnishment3', Garnishment3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GarnishmentType1 with content type ELEMENT_ONLY
class GarnishmentType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GarnishmentType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GarnishmentType1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 547, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdOrPrtry uses Python identifier CdOrPrtry
    __CdOrPrtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), 'CdOrPrtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_GarnishmentType1_urnCBIxsdCBIPaymentRequest_00_04_01CdOrPrtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 549, 3), )

    
    CdOrPrtry = property(__CdOrPrtry.value, __CdOrPrtry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_GarnishmentType1_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 550, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __CdOrPrtry.name() : __CdOrPrtry,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GarnishmentType1 = GarnishmentType1
Namespace.addCategoryObject('typeBinding', 'GarnishmentType1', GarnishmentType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GarnishmentType1Choice with content type ELEMENT_ONLY
class GarnishmentType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GarnishmentType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GarnishmentType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 553, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_GarnishmentType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 555, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_GarnishmentType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 556, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GarnishmentType1Choice = GarnishmentType1Choice
Namespace.addCategoryObject('typeBinding', 'GarnishmentType1Choice', GarnishmentType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericIdentification3 with content type ELEMENT_ONLY
class GenericIdentification3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericIdentification3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericIdentification3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 559, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 561, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericIdentification3_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 562, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericIdentification3 = GenericIdentification3
Namespace.addCategoryObject('typeBinding', 'GenericIdentification3', GenericIdentification3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericIdentification30 with content type ELEMENT_ONLY
class GenericIdentification30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericIdentification30 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericIdentification30')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 565, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericIdentification30_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 567, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericIdentification30_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 568, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SchmeNm uses Python identifier SchmeNm
    __SchmeNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), 'SchmeNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericIdentification30_urnCBIxsdCBIPaymentRequest_00_04_01SchmeNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 569, 3), )

    
    SchmeNm = property(__SchmeNm.value, __SchmeNm.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __Issr.name() : __Issr,
        __SchmeNm.name() : __SchmeNm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericIdentification30 = GenericIdentification30
Namespace.addCategoryObject('typeBinding', 'GenericIdentification30', GenericIdentification30)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericOrganisationIdentification1 with content type ELEMENT_ONLY
class GenericOrganisationIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericOrganisationIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericOrganisationIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 572, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 574, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SchmeNm uses Python identifier SchmeNm
    __SchmeNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), 'SchmeNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01SchmeNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 575, 3), )

    
    SchmeNm = property(__SchmeNm.value, __SchmeNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericOrganisationIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 576, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __SchmeNm.name() : __SchmeNm,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericOrganisationIdentification1 = GenericOrganisationIdentification1
Namespace.addCategoryObject('typeBinding', 'GenericOrganisationIdentification1', GenericOrganisationIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericPersonIdentification1 with content type ELEMENT_ONLY
class GenericPersonIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GenericPersonIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericPersonIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 579, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 581, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SchmeNm uses Python identifier SchmeNm
    __SchmeNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), 'SchmeNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01SchmeNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 582, 3), )

    
    SchmeNm = property(__SchmeNm.value, __SchmeNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_GenericPersonIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 583, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __SchmeNm.name() : __SchmeNm,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericPersonIdentification1 = GenericPersonIdentification1
Namespace.addCategoryObject('typeBinding', 'GenericPersonIdentification1', GenericPersonIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrganisationIdentification4 with content type ELEMENT_ONLY
class OrganisationIdentification4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrganisationIdentification4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationIdentification4')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 586, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AnyBIC uses Python identifier AnyBIC
    __AnyBIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), 'AnyBIC', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01AnyBIC', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 588, 3), )

    
    AnyBIC = property(__AnyBIC.value, __AnyBIC.set, None, ' CHAN: Name Changed into AnyBIC and Type Changed into AnyBICDec2014Identifier for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01LEI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 593, 3), )

    
    LEI = property(__LEI.value, __LEI.set, None, ' CHAN: Field included for v2019 ISO message migration ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentification4_urnCBIxsdCBIPaymentRequest_00_04_01Othr', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 598, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __AnyBIC.name() : __AnyBIC,
        __LEI.name() : __LEI,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganisationIdentification4 = OrganisationIdentification4
Namespace.addCategoryObject('typeBinding', 'OrganisationIdentification4', OrganisationIdentification4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrganisationIdentification29 with content type ELEMENT_ONLY
class OrganisationIdentification29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrganisationIdentification29 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationIdentification29')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 601, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AnyBIC uses Python identifier AnyBIC
    __AnyBIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), 'AnyBIC', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentification29_urnCBIxsdCBIPaymentRequest_00_04_01AnyBIC', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 603, 3), )

    
    AnyBIC = property(__AnyBIC.value, __AnyBIC.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LEI uses Python identifier LEI
    __LEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LEI'), 'LEI', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentification29_urnCBIxsdCBIPaymentRequest_00_04_01LEI', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 604, 3), )

    
    LEI = property(__LEI.value, __LEI.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentification29_urnCBIxsdCBIPaymentRequest_00_04_01Othr', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 605, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __AnyBIC.name() : __AnyBIC,
        __LEI.name() : __LEI,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganisationIdentification29 = OrganisationIdentification29
Namespace.addCategoryObject('typeBinding', 'OrganisationIdentification29', OrganisationIdentification29)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrganisationIdentificationSchemeName1Choice with content type ELEMENT_ONLY
class OrganisationIdentificationSchemeName1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrganisationIdentificationSchemeName1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationIdentificationSchemeName1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 608, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 611, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_OrganisationIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 612, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganisationIdentificationSchemeName1Choice = OrganisationIdentificationSchemeName1Choice
Namespace.addCategoryObject('typeBinding', 'OrganisationIdentificationSchemeName1Choice', OrganisationIdentificationSchemeName1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OtherContact1 with content type ELEMENT_ONLY
class OtherContact1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OtherContact1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OtherContact1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 616, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ChanlTp uses Python identifier ChanlTp
    __ChanlTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChanlTp'), 'ChanlTp', '__urnCBIxsdCBIPaymentRequest_00_04_01_OtherContact1_urnCBIxsdCBIPaymentRequest_00_04_01ChanlTp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 618, 3), )

    
    ChanlTp = property(__ChanlTp.value, __ChanlTp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_OtherContact1_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 619, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __ChanlTp.name() : __ChanlTp,
        __Id.name() : __Id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OtherContact1 = OtherContact1
Namespace.addCategoryObject('typeBinding', 'OtherContact1', OtherContact1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PartyIdentification135 with content type ELEMENT_ONLY
class PartyIdentification135 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PartyIdentification135 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification135')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 622, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_PartyIdentification135_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 624, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstlAdr uses Python identifier PstlAdr
    __PstlAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), 'PstlAdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_PartyIdentification135_urnCBIxsdCBIPaymentRequest_00_04_01PstlAdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 625, 3), )

    
    PstlAdr = property(__PstlAdr.value, __PstlAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnCBIxsdCBIPaymentRequest_00_04_01_PartyIdentification135_urnCBIxsdCBIPaymentRequest_00_04_01Id', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 626, 3), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtryOfRes uses Python identifier CtryOfRes
    __CtryOfRes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), 'CtryOfRes', '__urnCBIxsdCBIPaymentRequest_00_04_01_PartyIdentification135_urnCBIxsdCBIPaymentRequest_00_04_01CtryOfRes', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 627, 3), )

    
    CtryOfRes = property(__CtryOfRes.value, __CtryOfRes.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtctDtls uses Python identifier CtctDtls
    __CtctDtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls'), 'CtctDtls', '__urnCBIxsdCBIPaymentRequest_00_04_01_PartyIdentification135_urnCBIxsdCBIPaymentRequest_00_04_01CtctDtls', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 628, 3), )

    
    CtctDtls = property(__CtctDtls.value, __CtctDtls.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __PstlAdr.name() : __PstlAdr,
        __Id.name() : __Id,
        __CtryOfRes.name() : __CtryOfRes,
        __CtctDtls.name() : __CtctDtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification135 = PartyIdentification135
Namespace.addCategoryObject('typeBinding', 'PartyIdentification135', PartyIdentification135)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Contact4 with content type ELEMENT_ONLY
class Contact4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Contact4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Contact4')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 631, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}NmPrfx uses Python identifier NmPrfx
    __NmPrfx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NmPrfx'), 'NmPrfx', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01NmPrfx', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 633, 3), )

    
    NmPrfx = property(__NmPrfx.value, __NmPrfx.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 634, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PhneNb uses Python identifier PhneNb
    __PhneNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PhneNb'), 'PhneNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01PhneNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 635, 3), )

    
    PhneNb = property(__PhneNb.value, __PhneNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}MobNb uses Python identifier MobNb
    __MobNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MobNb'), 'MobNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01MobNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 636, 3), )

    
    MobNb = property(__MobNb.value, __MobNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FaxNb uses Python identifier FaxNb
    __FaxNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FaxNb'), 'FaxNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01FaxNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 637, 3), )

    
    FaxNb = property(__FaxNb.value, __FaxNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}EmailAdr uses Python identifier EmailAdr
    __EmailAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmailAdr'), 'EmailAdr', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01EmailAdr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 638, 3), )

    
    EmailAdr = property(__EmailAdr.value, __EmailAdr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}EmailPurp uses Python identifier EmailPurp
    __EmailPurp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmailPurp'), 'EmailPurp', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01EmailPurp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 639, 3), )

    
    EmailPurp = property(__EmailPurp.value, __EmailPurp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}JobTitl uses Python identifier JobTitl
    __JobTitl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JobTitl'), 'JobTitl', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01JobTitl', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 640, 3), )

    
    JobTitl = property(__JobTitl.value, __JobTitl.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Rspnsblty uses Python identifier Rspnsblty
    __Rspnsblty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rspnsblty'), 'Rspnsblty', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01Rspnsblty', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 641, 3), )

    
    Rspnsblty = property(__Rspnsblty.value, __Rspnsblty.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dept uses Python identifier Dept
    __Dept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dept'), 'Dept', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01Dept', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 642, 3), )

    
    Dept = property(__Dept.value, __Dept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01Othr', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 643, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PrefrdMtd uses Python identifier PrefrdMtd
    __PrefrdMtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrefrdMtd'), 'PrefrdMtd', '__urnCBIxsdCBIPaymentRequest_00_04_01_Contact4_urnCBIxsdCBIPaymentRequest_00_04_01PrefrdMtd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 644, 3), )

    
    PrefrdMtd = property(__PrefrdMtd.value, __PrefrdMtd.set, None, None)

    _ElementMap.update({
        __NmPrfx.name() : __NmPrfx,
        __Nm.name() : __Nm,
        __PhneNb.name() : __PhneNb,
        __MobNb.name() : __MobNb,
        __FaxNb.name() : __FaxNb,
        __EmailAdr.name() : __EmailAdr,
        __EmailPurp.name() : __EmailPurp,
        __JobTitl.name() : __JobTitl,
        __Rspnsblty.name() : __Rspnsblty,
        __Dept.name() : __Dept,
        __Othr.name() : __Othr,
        __PrefrdMtd.name() : __PrefrdMtd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Contact4 = Contact4
Namespace.addCategoryObject('typeBinding', 'Contact4', Contact4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Party38Choice with content type ELEMENT_ONLY
class Party38Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Party38Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party38Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 647, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId', '__urnCBIxsdCBIPaymentRequest_00_04_01_Party38Choice_urnCBIxsdCBIPaymentRequest_00_04_01OrgId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 649, 3), )

    
    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PrvtId uses Python identifier PrvtId
    __PrvtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), 'PrvtId', '__urnCBIxsdCBIPaymentRequest_00_04_01_Party38Choice_urnCBIxsdCBIPaymentRequest_00_04_01PrvtId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 650, 3), )

    
    PrvtId = property(__PrvtId.value, __PrvtId.set, None, None)

    _ElementMap.update({
        __OrgId.name() : __OrgId,
        __PrvtId.name() : __PrvtId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Party38Choice = Party38Choice
Namespace.addCategoryObject('typeBinding', 'Party38Choice', Party38Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PaymentIdentification1 with content type ELEMENT_ONLY
class PaymentIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PaymentIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 653, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstrId uses Python identifier InstrId
    __InstrId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrId'), 'InstrId', '__urnCBIxsdCBIPaymentRequest_00_04_01_PaymentIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01InstrId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 655, 3), )

    
    InstrId = property(__InstrId.value, __InstrId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}EndToEndId uses Python identifier EndToEndId
    __EndToEndId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndToEndId'), 'EndToEndId', '__urnCBIxsdCBIPaymentRequest_00_04_01_PaymentIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01EndToEndId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 656, 3), )

    
    EndToEndId = property(__EndToEndId.value, __EndToEndId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}UETR uses Python identifier UETR
    __UETR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UETR'), 'UETR', '__urnCBIxsdCBIPaymentRequest_00_04_01_PaymentIdentification1_urnCBIxsdCBIPaymentRequest_00_04_01UETR', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 657, 3), )

    
    UETR = property(__UETR.value, __UETR.set, None, ' CHAN: Field included for v2019 ISO message migration ')

    _ElementMap.update({
        __InstrId.name() : __InstrId,
        __EndToEndId.name() : __EndToEndId,
        __UETR.name() : __UETR
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PaymentIdentification1 = PaymentIdentification1
Namespace.addCategoryObject('typeBinding', 'PaymentIdentification1', PaymentIdentification1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PersonIdentification13 with content type ELEMENT_ONLY
class PersonIdentification13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PersonIdentification13 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonIdentification13')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 664, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DtAndPlcOfBirth uses Python identifier DtAndPlcOfBirth
    __DtAndPlcOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth'), 'DtAndPlcOfBirth', '__urnCBIxsdCBIPaymentRequest_00_04_01_PersonIdentification13_urnCBIxsdCBIPaymentRequest_00_04_01DtAndPlcOfBirth', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 666, 3), )

    
    DtAndPlcOfBirth = property(__DtAndPlcOfBirth.value, __DtAndPlcOfBirth.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr', '__urnCBIxsdCBIPaymentRequest_00_04_01_PersonIdentification13_urnCBIxsdCBIPaymentRequest_00_04_01Othr', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 667, 3), )

    
    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __DtAndPlcOfBirth.name() : __DtAndPlcOfBirth,
        __Othr.name() : __Othr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonIdentification13 = PersonIdentification13
Namespace.addCategoryObject('typeBinding', 'PersonIdentification13', PersonIdentification13)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PersonIdentificationSchemeName1Choice with content type ELEMENT_ONLY
class PersonIdentificationSchemeName1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PersonIdentificationSchemeName1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonIdentificationSchemeName1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 670, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_PersonIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 673, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_PersonIdentificationSchemeName1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 674, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PersonIdentificationSchemeName1Choice = PersonIdentificationSchemeName1Choice
Namespace.addCategoryObject('typeBinding', 'PersonIdentificationSchemeName1Choice', PersonIdentificationSchemeName1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PostalAddress24 with content type ELEMENT_ONLY
class PostalAddress24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PostalAddress24 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PostalAddress24')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 678, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdrTp uses Python identifier AdrTp
    __AdrTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdrTp'), 'AdrTp', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01AdrTp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 680, 3), )

    
    AdrTp = property(__AdrTp.value, __AdrTp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dept uses Python identifier Dept
    __Dept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dept'), 'Dept', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Dept', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 681, 3), )

    
    Dept = property(__Dept.value, __Dept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SubDept uses Python identifier SubDept
    __SubDept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubDept'), 'SubDept', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01SubDept', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 682, 3), )

    
    SubDept = property(__SubDept.value, __SubDept.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}StrtNm uses Python identifier StrtNm
    __StrtNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), 'StrtNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01StrtNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 683, 3), )

    
    StrtNm = property(__StrtNm.value, __StrtNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BldgNb uses Python identifier BldgNb
    __BldgNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BldgNb'), 'BldgNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01BldgNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 684, 3), )

    
    BldgNb = property(__BldgNb.value, __BldgNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}BldgNm uses Python identifier BldgNm
    __BldgNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BldgNm'), 'BldgNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01BldgNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 685, 3), )

    
    BldgNm = property(__BldgNm.value, __BldgNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Flr uses Python identifier Flr
    __Flr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Flr'), 'Flr', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Flr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 686, 3), )

    
    Flr = property(__Flr.value, __Flr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstBx uses Python identifier PstBx
    __PstBx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstBx'), 'PstBx', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01PstBx', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 687, 3), )

    
    PstBx = property(__PstBx.value, __PstBx.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Room uses Python identifier Room
    __Room = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Room'), 'Room', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Room', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 688, 3), )

    
    Room = property(__Room.value, __Room.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}PstCd uses Python identifier PstCd
    __PstCd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstCd'), 'PstCd', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01PstCd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 689, 3), )

    
    PstCd = property(__PstCd.value, __PstCd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TwnNm uses Python identifier TwnNm
    __TwnNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), 'TwnNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01TwnNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 690, 3), )

    
    TwnNm = property(__TwnNm.value, __TwnNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TwnLctnNm uses Python identifier TwnLctnNm
    __TwnLctnNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TwnLctnNm'), 'TwnLctnNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01TwnLctnNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 691, 3), )

    
    TwnLctnNm = property(__TwnLctnNm.value, __TwnLctnNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DstrctNm uses Python identifier DstrctNm
    __DstrctNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm'), 'DstrctNm', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01DstrctNm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 692, 3), )

    
    DstrctNm = property(__DstrctNm.value, __DstrctNm.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtrySubDvsn uses Python identifier CtrySubDvsn
    __CtrySubDvsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn'), 'CtrySubDvsn', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01CtrySubDvsn', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 693, 3), )

    
    CtrySubDvsn = property(__CtrySubDvsn.value, __CtrySubDvsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01Ctry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 694, 3), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdrLine uses Python identifier AdrLine
    __AdrLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdrLine'), 'AdrLine', '__urnCBIxsdCBIPaymentRequest_00_04_01_PostalAddress24_urnCBIxsdCBIPaymentRequest_00_04_01AdrLine', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 695, 3), )

    
    AdrLine = property(__AdrLine.value, __AdrLine.set, None, None)

    _ElementMap.update({
        __AdrTp.name() : __AdrTp,
        __Dept.name() : __Dept,
        __SubDept.name() : __SubDept,
        __StrtNm.name() : __StrtNm,
        __BldgNb.name() : __BldgNb,
        __BldgNm.name() : __BldgNm,
        __Flr.name() : __Flr,
        __PstBx.name() : __PstBx,
        __Room.name() : __Room,
        __PstCd.name() : __PstCd,
        __TwnNm.name() : __TwnNm,
        __TwnLctnNm.name() : __TwnLctnNm,
        __DstrctNm.name() : __DstrctNm,
        __CtrySubDvsn.name() : __CtrySubDvsn,
        __Ctry.name() : __Ctry,
        __AdrLine.name() : __AdrLine
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PostalAddress24 = PostalAddress24
Namespace.addCategoryObject('typeBinding', 'PostalAddress24', PostalAddress24)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstructionForCreditorAgent1 with content type ELEMENT_ONLY
class InstructionForCreditorAgent1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstructionForCreditorAgent1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstructionForCreditorAgent1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 698, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_InstructionForCreditorAgent1_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 700, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}InstrInf uses Python identifier InstrInf
    __InstrInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstrInf'), 'InstrInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_InstructionForCreditorAgent1_urnCBIxsdCBIPaymentRequest_00_04_01InstrInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 701, 3), )

    
    InstrInf = property(__InstrInf.value, __InstrInf.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __InstrInf.name() : __InstrInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InstructionForCreditorAgent1 = InstructionForCreditorAgent1
Namespace.addCategoryObject('typeBinding', 'InstructionForCreditorAgent1', InstructionForCreditorAgent1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Purpose1Choice with content type ELEMENT_ONLY
class Purpose1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Purpose1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Purpose1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 704, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_Purpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 707, 4), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_Purpose1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 708, 4), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Purpose1Choice = Purpose1Choice
Namespace.addCategoryObject('typeBinding', 'Purpose1Choice', Purpose1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RemittanceInformation16 with content type ELEMENT_ONLY
class RemittanceInformation16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RemittanceInformation16 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RemittanceInformation16')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 712, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Ustrd uses Python identifier Ustrd
    __Ustrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ustrd'), 'Ustrd', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01Ustrd', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 714, 3), )

    
    Ustrd = property(__Ustrd.value, __Ustrd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Strd uses Python identifier Strd
    __Strd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Strd'), 'Strd', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01Strd', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 715, 3), )

    
    Strd = property(__Strd.value, __Strd.set, None, None)

    _ElementMap.update({
        __Ustrd.name() : __Ustrd,
        __Strd.name() : __Strd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RemittanceInformation16 = RemittanceInformation16
Namespace.addCategoryObject('typeBinding', 'RemittanceInformation16', RemittanceInformation16)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReferredDocumentInformation7 with content type ELEMENT_ONLY
class ReferredDocumentInformation7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReferredDocumentInformation7 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferredDocumentInformation7')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 718, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 720, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nb uses Python identifier Nb
    __Nb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nb'), 'Nb', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Nb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 721, 3), )

    
    Nb = property(__Nb.value, __Nb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RltdDt uses Python identifier RltdDt
    __RltdDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RltdDt'), 'RltdDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentInformation7_urnCBIxsdCBIPaymentRequest_00_04_01RltdDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 722, 3), )

    
    RltdDt = property(__RltdDt.value, __RltdDt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}LineDtls uses Python identifier LineDtls
    __LineDtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LineDtls'), 'LineDtls', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentInformation7_urnCBIxsdCBIPaymentRequest_00_04_01LineDtls', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 723, 3), )

    
    LineDtls = property(__LineDtls.value, __LineDtls.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Nb.name() : __Nb,
        __RltdDt.name() : __RltdDt,
        __LineDtls.name() : __LineDtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferredDocumentInformation7 = ReferredDocumentInformation7
Namespace.addCategoryObject('typeBinding', 'ReferredDocumentInformation7', ReferredDocumentInformation7)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReferredDocumentType3Choice with content type ELEMENT_ONLY
class ReferredDocumentType3Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReferredDocumentType3Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferredDocumentType3Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 726, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentType3Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 728, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentType3Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 729, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferredDocumentType3Choice = ReferredDocumentType3Choice
Namespace.addCategoryObject('typeBinding', 'ReferredDocumentType3Choice', ReferredDocumentType3Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReferredDocumentType4 with content type ELEMENT_ONLY
class ReferredDocumentType4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ReferredDocumentType4 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferredDocumentType4')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 732, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdOrPrtry uses Python identifier CdOrPrtry
    __CdOrPrtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), 'CdOrPrtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentType4_urnCBIxsdCBIPaymentRequest_00_04_01CdOrPrtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 734, 3), )

    
    CdOrPrtry = property(__CdOrPrtry.value, __CdOrPrtry.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnCBIxsdCBIPaymentRequest_00_04_01_ReferredDocumentType4_urnCBIxsdCBIPaymentRequest_00_04_01Issr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 735, 3), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __CdOrPrtry.name() : __CdOrPrtry,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferredDocumentType4 = ReferredDocumentType4
Namespace.addCategoryObject('typeBinding', 'ReferredDocumentType4', ReferredDocumentType4)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RemittanceAmount2 with content type ELEMENT_ONLY
class RemittanceAmount2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RemittanceAmount2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RemittanceAmount2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 738, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DuePyblAmt uses Python identifier DuePyblAmt
    __DuePyblAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt'), 'DuePyblAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount2_urnCBIxsdCBIPaymentRequest_00_04_01DuePyblAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 740, 3), )

    
    DuePyblAmt = property(__DuePyblAmt.value, __DuePyblAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DscntApldAmt uses Python identifier DscntApldAmt
    __DscntApldAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt'), 'DscntApldAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount2_urnCBIxsdCBIPaymentRequest_00_04_01DscntApldAmt', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 741, 3), )

    
    DscntApldAmt = property(__DscntApldAmt.value, __DscntApldAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtNoteAmt uses Python identifier CdtNoteAmt
    __CdtNoteAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt'), 'CdtNoteAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount2_urnCBIxsdCBIPaymentRequest_00_04_01CdtNoteAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 742, 3), )

    
    CdtNoteAmt = property(__CdtNoteAmt.value, __CdtNoteAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmt uses Python identifier TaxAmt
    __TaxAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), 'TaxAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount2_urnCBIxsdCBIPaymentRequest_00_04_01TaxAmt', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 743, 3), )

    
    TaxAmt = property(__TaxAmt.value, __TaxAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdjstmntAmtAndRsn uses Python identifier AdjstmntAmtAndRsn
    __AdjstmntAmtAndRsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn'), 'AdjstmntAmtAndRsn', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount2_urnCBIxsdCBIPaymentRequest_00_04_01AdjstmntAmtAndRsn', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 744, 3), )

    
    AdjstmntAmtAndRsn = property(__AdjstmntAmtAndRsn.value, __AdjstmntAmtAndRsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RmtdAmt uses Python identifier RmtdAmt
    __RmtdAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), 'RmtdAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount2_urnCBIxsdCBIPaymentRequest_00_04_01RmtdAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 745, 3), )

    
    RmtdAmt = property(__RmtdAmt.value, __RmtdAmt.set, None, None)

    _ElementMap.update({
        __DuePyblAmt.name() : __DuePyblAmt,
        __DscntApldAmt.name() : __DscntApldAmt,
        __CdtNoteAmt.name() : __CdtNoteAmt,
        __TaxAmt.name() : __TaxAmt,
        __AdjstmntAmtAndRsn.name() : __AdjstmntAmtAndRsn,
        __RmtdAmt.name() : __RmtdAmt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RemittanceAmount2 = RemittanceAmount2
Namespace.addCategoryObject('typeBinding', 'RemittanceAmount2', RemittanceAmount2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RemittanceAmount3 with content type ELEMENT_ONLY
class RemittanceAmount3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RemittanceAmount3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RemittanceAmount3')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 748, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DuePyblAmt uses Python identifier DuePyblAmt
    __DuePyblAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt'), 'DuePyblAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount3_urnCBIxsdCBIPaymentRequest_00_04_01DuePyblAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 750, 3), )

    
    DuePyblAmt = property(__DuePyblAmt.value, __DuePyblAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DscntApldAmt uses Python identifier DscntApldAmt
    __DscntApldAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt'), 'DscntApldAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount3_urnCBIxsdCBIPaymentRequest_00_04_01DscntApldAmt', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 751, 3), )

    
    DscntApldAmt = property(__DscntApldAmt.value, __DscntApldAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtNoteAmt uses Python identifier CdtNoteAmt
    __CdtNoteAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt'), 'CdtNoteAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount3_urnCBIxsdCBIPaymentRequest_00_04_01CdtNoteAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 752, 3), )

    
    CdtNoteAmt = property(__CdtNoteAmt.value, __CdtNoteAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmt uses Python identifier TaxAmt
    __TaxAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), 'TaxAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount3_urnCBIxsdCBIPaymentRequest_00_04_01TaxAmt', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 753, 3), )

    
    TaxAmt = property(__TaxAmt.value, __TaxAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdjstmntAmtAndRsn uses Python identifier AdjstmntAmtAndRsn
    __AdjstmntAmtAndRsn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn'), 'AdjstmntAmtAndRsn', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount3_urnCBIxsdCBIPaymentRequest_00_04_01AdjstmntAmtAndRsn', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 754, 3), )

    
    AdjstmntAmtAndRsn = property(__AdjstmntAmtAndRsn.value, __AdjstmntAmtAndRsn.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RmtdAmt uses Python identifier RmtdAmt
    __RmtdAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), 'RmtdAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_RemittanceAmount3_urnCBIxsdCBIPaymentRequest_00_04_01RmtdAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 755, 3), )

    
    RmtdAmt = property(__RmtdAmt.value, __RmtdAmt.set, None, None)

    _ElementMap.update({
        __DuePyblAmt.name() : __DuePyblAmt,
        __DscntApldAmt.name() : __DscntApldAmt,
        __CdtNoteAmt.name() : __CdtNoteAmt,
        __TaxAmt.name() : __TaxAmt,
        __AdjstmntAmtAndRsn.name() : __AdjstmntAmtAndRsn,
        __RmtdAmt.name() : __RmtdAmt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RemittanceAmount3 = RemittanceAmount3
Namespace.addCategoryObject('typeBinding', 'RemittanceAmount3', RemittanceAmount3)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}StructuredRemittanceInformation16 with content type ELEMENT_ONLY
class StructuredRemittanceInformation16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}StructuredRemittanceInformation16 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StructuredRemittanceInformation16')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 758, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RfrdDocInf uses Python identifier RfrdDocInf
    __RfrdDocInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocInf'), 'RfrdDocInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01RfrdDocInf', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 760, 3), )

    
    RfrdDocInf = property(__RfrdDocInf.value, __RfrdDocInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RfrdDocAmt uses Python identifier RfrdDocAmt
    __RfrdDocAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocAmt'), 'RfrdDocAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01RfrdDocAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 761, 3), )

    
    RfrdDocAmt = property(__RfrdDocAmt.value, __RfrdDocAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CdtrRefInf uses Python identifier CdtrRefInf
    __CdtrRefInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtrRefInf'), 'CdtrRefInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01CdtrRefInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 762, 3), )

    
    CdtrRefInf = property(__CdtrRefInf.value, __CdtrRefInf.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Invcr uses Python identifier Invcr
    __Invcr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Invcr'), 'Invcr', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01Invcr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 763, 3), )

    
    Invcr = property(__Invcr.value, __Invcr.set, None, ' CHAN: Changed data type for migration to v2019 ISO Message ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Invcee uses Python identifier Invcee
    __Invcee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Invcee'), 'Invcee', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01Invcee', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 768, 3), )

    
    Invcee = property(__Invcee.value, __Invcee.set, None, ' CHAN: Changed data type for migration to v2019 ISO Message ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxRmt uses Python identifier TaxRmt
    __TaxRmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxRmt'), 'TaxRmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01TaxRmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 773, 3), )

    
    TaxRmt = property(__TaxRmt.value, __TaxRmt.set, None, ' CHAN - Complex structure included for the migration to v2019 ISO message ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}GrnshmtRmt uses Python identifier GrnshmtRmt
    __GrnshmtRmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GrnshmtRmt'), 'GrnshmtRmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01GrnshmtRmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 778, 3), )

    
    GrnshmtRmt = property(__GrnshmtRmt.value, __GrnshmtRmt.set, None, ' CHAN - Complex structure included for the migration to v2019 ISO message ')

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AddtlRmtInf uses Python identifier AddtlRmtInf
    __AddtlRmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddtlRmtInf'), 'AddtlRmtInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_StructuredRemittanceInformation16_urnCBIxsdCBIPaymentRequest_00_04_01AddtlRmtInf', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 783, 3), )

    
    AddtlRmtInf = property(__AddtlRmtInf.value, __AddtlRmtInf.set, None, None)

    _ElementMap.update({
        __RfrdDocInf.name() : __RfrdDocInf,
        __RfrdDocAmt.name() : __RfrdDocAmt,
        __CdtrRefInf.name() : __CdtrRefInf,
        __Invcr.name() : __Invcr,
        __Invcee.name() : __Invcee,
        __TaxRmt.name() : __TaxRmt,
        __GrnshmtRmt.name() : __GrnshmtRmt,
        __AddtlRmtInf.name() : __AddtlRmtInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StructuredRemittanceInformation16 = StructuredRemittanceInformation16
Namespace.addCategoryObject('typeBinding', 'StructuredRemittanceInformation16', StructuredRemittanceInformation16)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmount2 with content type ELEMENT_ONLY
class TaxAmount2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmount2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxAmount2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 786, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Rate uses Python identifier Rate
    __Rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rate'), 'Rate', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmount2_urnCBIxsdCBIPaymentRequest_00_04_01Rate', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 788, 3), )

    
    Rate = property(__Rate.value, __Rate.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxblBaseAmt uses Python identifier TaxblBaseAmt
    __TaxblBaseAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxblBaseAmt'), 'TaxblBaseAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmount2_urnCBIxsdCBIPaymentRequest_00_04_01TaxblBaseAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 789, 3), )

    
    TaxblBaseAmt = property(__TaxblBaseAmt.value, __TaxblBaseAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TtlAmt uses Python identifier TtlAmt
    __TtlAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlAmt'), 'TtlAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmount2_urnCBIxsdCBIPaymentRequest_00_04_01TtlAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 790, 3), )

    
    TtlAmt = property(__TtlAmt.value, __TtlAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dtls uses Python identifier Dtls
    __Dtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dtls'), 'Dtls', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmount2_urnCBIxsdCBIPaymentRequest_00_04_01Dtls', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 791, 3), )

    
    Dtls = property(__Dtls.value, __Dtls.set, None, None)

    _ElementMap.update({
        __Rate.name() : __Rate,
        __TaxblBaseAmt.name() : __TaxblBaseAmt,
        __TtlAmt.name() : __TtlAmt,
        __Dtls.name() : __Dtls
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxAmount2 = TaxAmount2
Namespace.addCategoryObject('typeBinding', 'TaxAmount2', TaxAmount2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmountAndType1 with content type ELEMENT_ONLY
class TaxAmountAndType1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmountAndType1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxAmountAndType1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 794, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmountAndType1_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 796, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmountAndType1_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 797, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Amt.name() : __Amt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxAmountAndType1 = TaxAmountAndType1
Namespace.addCategoryObject('typeBinding', 'TaxAmountAndType1', TaxAmountAndType1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmountType1Choice with content type ELEMENT_ONLY
class TaxAmountType1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmountType1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxAmountType1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 800, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cd uses Python identifier Cd
    __Cd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cd'), 'Cd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmountType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Cd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 802, 3), )

    
    Cd = property(__Cd.value, __Cd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prtry uses Python identifier Prtry
    __Prtry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), 'Prtry', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAmountType1Choice_urnCBIxsdCBIPaymentRequest_00_04_01Prtry', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 803, 3), )

    
    Prtry = property(__Prtry.value, __Prtry.set, None, None)

    _ElementMap.update({
        __Cd.name() : __Cd,
        __Prtry.name() : __Prtry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxAmountType1Choice = TaxAmountType1Choice
Namespace.addCategoryObject('typeBinding', 'TaxAmountType1Choice', TaxAmountType1Choice)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAuthorisation1 with content type ELEMENT_ONLY
class TaxAuthorisation1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAuthorisation1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxAuthorisation1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 806, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Titl uses Python identifier Titl
    __Titl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Titl'), 'Titl', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAuthorisation1_urnCBIxsdCBIPaymentRequest_00_04_01Titl', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 808, 3), )

    
    Titl = property(__Titl.value, __Titl.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxAuthorisation1_urnCBIxsdCBIPaymentRequest_00_04_01Nm', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 809, 3), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    _ElementMap.update({
        __Titl.name() : __Titl,
        __Nm.name() : __Nm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxAuthorisation1 = TaxAuthorisation1
Namespace.addCategoryObject('typeBinding', 'TaxAuthorisation1', TaxAuthorisation1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxInformation7 with content type ELEMENT_ONLY
class TaxInformation7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxInformation7 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxInformation7')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 812, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cdtr uses Python identifier Cdtr
    __Cdtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), 'Cdtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Cdtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 814, 3), )

    
    Cdtr = property(__Cdtr.value, __Cdtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dbtr uses Python identifier Dbtr
    __Dbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), 'Dbtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Dbtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 815, 3), )

    
    Dbtr = property(__Dbtr.value, __Dbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}UltmtDbtr uses Python identifier UltmtDbtr
    __UltmtDbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), 'UltmtDbtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01UltmtDbtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 816, 3), )

    
    UltmtDbtr = property(__UltmtDbtr.value, __UltmtDbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdmstnZone uses Python identifier AdmstnZone
    __AdmstnZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdmstnZone'), 'AdmstnZone', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01AdmstnZone', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 817, 3), )

    
    AdmstnZone = property(__AdmstnZone.value, __AdmstnZone.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RefNb uses Python identifier RefNb
    __RefNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RefNb'), 'RefNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01RefNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 818, 3), )

    
    RefNb = property(__RefNb.value, __RefNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Mtd uses Python identifier Mtd
    __Mtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mtd'), 'Mtd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Mtd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 819, 3), )

    
    Mtd = property(__Mtd.value, __Mtd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TtlTaxblBaseAmt uses Python identifier TtlTaxblBaseAmt
    __TtlTaxblBaseAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxblBaseAmt'), 'TtlTaxblBaseAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01TtlTaxblBaseAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 820, 3), )

    
    TtlTaxblBaseAmt = property(__TtlTaxblBaseAmt.value, __TtlTaxblBaseAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TtlTaxAmt uses Python identifier TtlTaxAmt
    __TtlTaxAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxAmt'), 'TtlTaxAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01TtlTaxAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 821, 3), )

    
    TtlTaxAmt = property(__TtlTaxAmt.value, __TtlTaxAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dt uses Python identifier Dt
    __Dt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dt'), 'Dt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Dt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 822, 3), )

    
    Dt = property(__Dt.value, __Dt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SeqNb uses Python identifier SeqNb
    __SeqNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SeqNb'), 'SeqNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01SeqNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 823, 3), )

    
    SeqNb = property(__SeqNb.value, __SeqNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Rcrd uses Python identifier Rcrd
    __Rcrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rcrd'), 'Rcrd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation7_urnCBIxsdCBIPaymentRequest_00_04_01Rcrd', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 824, 3), )

    
    Rcrd = property(__Rcrd.value, __Rcrd.set, None, None)

    _ElementMap.update({
        __Cdtr.name() : __Cdtr,
        __Dbtr.name() : __Dbtr,
        __UltmtDbtr.name() : __UltmtDbtr,
        __AdmstnZone.name() : __AdmstnZone,
        __RefNb.name() : __RefNb,
        __Mtd.name() : __Mtd,
        __TtlTaxblBaseAmt.name() : __TtlTaxblBaseAmt,
        __TtlTaxAmt.name() : __TtlTaxAmt,
        __Dt.name() : __Dt,
        __SeqNb.name() : __SeqNb,
        __Rcrd.name() : __Rcrd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxInformation7 = TaxInformation7
Namespace.addCategoryObject('typeBinding', 'TaxInformation7', TaxInformation7)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxInformation8 with content type ELEMENT_ONLY
class TaxInformation8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxInformation8 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxInformation8')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 827, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Cdtr uses Python identifier Cdtr
    __Cdtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), 'Cdtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01Cdtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 829, 3), )

    
    Cdtr = property(__Cdtr.value, __Cdtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dbtr uses Python identifier Dbtr
    __Dbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), 'Dbtr', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01Dbtr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 830, 3), )

    
    Dbtr = property(__Dbtr.value, __Dbtr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AdmstnZone uses Python identifier AdmstnZone
    __AdmstnZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdmstnZone'), 'AdmstnZone', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01AdmstnZone', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 831, 3), )

    
    AdmstnZone = property(__AdmstnZone.value, __AdmstnZone.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RefNb uses Python identifier RefNb
    __RefNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RefNb'), 'RefNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01RefNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 832, 3), )

    
    RefNb = property(__RefNb.value, __RefNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Mtd uses Python identifier Mtd
    __Mtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mtd'), 'Mtd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01Mtd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 833, 3), )

    
    Mtd = property(__Mtd.value, __Mtd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TtlTaxblBaseAmt uses Python identifier TtlTaxblBaseAmt
    __TtlTaxblBaseAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxblBaseAmt'), 'TtlTaxblBaseAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01TtlTaxblBaseAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 834, 3), )

    
    TtlTaxblBaseAmt = property(__TtlTaxblBaseAmt.value, __TtlTaxblBaseAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TtlTaxAmt uses Python identifier TtlTaxAmt
    __TtlTaxAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxAmt'), 'TtlTaxAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01TtlTaxAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 835, 3), )

    
    TtlTaxAmt = property(__TtlTaxAmt.value, __TtlTaxAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Dt uses Python identifier Dt
    __Dt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dt'), 'Dt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01Dt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 836, 3), )

    
    Dt = property(__Dt.value, __Dt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}SeqNb uses Python identifier SeqNb
    __SeqNb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SeqNb'), 'SeqNb', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01SeqNb', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 837, 3), )

    
    SeqNb = property(__SeqNb.value, __SeqNb.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Rcrd uses Python identifier Rcrd
    __Rcrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rcrd'), 'Rcrd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxInformation8_urnCBIxsdCBIPaymentRequest_00_04_01Rcrd', True, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 838, 3), )

    
    Rcrd = property(__Rcrd.value, __Rcrd.set, None, None)

    _ElementMap.update({
        __Cdtr.name() : __Cdtr,
        __Dbtr.name() : __Dbtr,
        __AdmstnZone.name() : __AdmstnZone,
        __RefNb.name() : __RefNb,
        __Mtd.name() : __Mtd,
        __TtlTaxblBaseAmt.name() : __TtlTaxblBaseAmt,
        __TtlTaxAmt.name() : __TtlTaxAmt,
        __Dt.name() : __Dt,
        __SeqNb.name() : __SeqNb,
        __Rcrd.name() : __Rcrd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxInformation8 = TaxInformation8
Namespace.addCategoryObject('typeBinding', 'TaxInformation8', TaxInformation8)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxParty1 with content type ELEMENT_ONLY
class TaxParty1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxParty1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxParty1')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 841, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxId uses Python identifier TaxId
    __TaxId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxId'), 'TaxId', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty1_urnCBIxsdCBIPaymentRequest_00_04_01TaxId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 843, 3), )

    
    TaxId = property(__TaxId.value, __TaxId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RegnId uses Python identifier RegnId
    __RegnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RegnId'), 'RegnId', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty1_urnCBIxsdCBIPaymentRequest_00_04_01RegnId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 844, 3), )

    
    RegnId = property(__RegnId.value, __RegnId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxTp uses Python identifier TaxTp
    __TaxTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxTp'), 'TaxTp', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty1_urnCBIxsdCBIPaymentRequest_00_04_01TaxTp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 845, 3), )

    
    TaxTp = property(__TaxTp.value, __TaxTp.set, None, None)

    _ElementMap.update({
        __TaxId.name() : __TaxId,
        __RegnId.name() : __RegnId,
        __TaxTp.name() : __TaxTp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxParty1 = TaxParty1
Namespace.addCategoryObject('typeBinding', 'TaxParty1', TaxParty1)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxParty2 with content type ELEMENT_ONLY
class TaxParty2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxParty2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxParty2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 848, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxId uses Python identifier TaxId
    __TaxId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxId'), 'TaxId', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty2_urnCBIxsdCBIPaymentRequest_00_04_01TaxId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 850, 3), )

    
    TaxId = property(__TaxId.value, __TaxId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}RegnId uses Python identifier RegnId
    __RegnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RegnId'), 'RegnId', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty2_urnCBIxsdCBIPaymentRequest_00_04_01RegnId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 851, 3), )

    
    RegnId = property(__RegnId.value, __RegnId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxTp uses Python identifier TaxTp
    __TaxTp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxTp'), 'TaxTp', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty2_urnCBIxsdCBIPaymentRequest_00_04_01TaxTp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 852, 3), )

    
    TaxTp = property(__TaxTp.value, __TaxTp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Authstn uses Python identifier Authstn
    __Authstn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Authstn'), 'Authstn', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxParty2_urnCBIxsdCBIPaymentRequest_00_04_01Authstn', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 853, 3), )

    
    Authstn = property(__Authstn.value, __Authstn.set, None, None)

    _ElementMap.update({
        __TaxId.name() : __TaxId,
        __RegnId.name() : __RegnId,
        __TaxTp.name() : __TaxTp,
        __Authstn.name() : __Authstn
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxParty2 = TaxParty2
Namespace.addCategoryObject('typeBinding', 'TaxParty2', TaxParty2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxPeriod2 with content type ELEMENT_ONLY
class TaxPeriod2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxPeriod2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxPeriod2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 856, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Yr uses Python identifier Yr
    __Yr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Yr'), 'Yr', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxPeriod2_urnCBIxsdCBIPaymentRequest_00_04_01Yr', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 858, 3), )

    
    Yr = property(__Yr.value, __Yr.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxPeriod2_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 859, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FrToDt uses Python identifier FrToDt
    __FrToDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrToDt'), 'FrToDt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxPeriod2_urnCBIxsdCBIPaymentRequest_00_04_01FrToDt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 860, 3), )

    
    FrToDt = property(__FrToDt.value, __FrToDt.set, None, None)

    _ElementMap.update({
        __Yr.name() : __Yr,
        __Tp.name() : __Tp,
        __FrToDt.name() : __FrToDt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxPeriod2 = TaxPeriod2
Namespace.addCategoryObject('typeBinding', 'TaxPeriod2', TaxPeriod2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxRecord2 with content type ELEMENT_ONLY
class TaxRecord2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxRecord2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxRecord2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 863, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Tp uses Python identifier Tp
    __Tp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tp'), 'Tp', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01Tp', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 865, 3), )

    
    Tp = property(__Tp.value, __Tp.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Ctgy uses Python identifier Ctgy
    __Ctgy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctgy'), 'Ctgy', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01Ctgy', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 866, 3), )

    
    Ctgy = property(__Ctgy.value, __Ctgy.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CtgyDtls uses Python identifier CtgyDtls
    __CtgyDtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtgyDtls'), 'CtgyDtls', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01CtgyDtls', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 867, 3), )

    
    CtgyDtls = property(__CtgyDtls.value, __CtgyDtls.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}DbtrSts uses Python identifier DbtrSts
    __DbtrSts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrSts'), 'DbtrSts', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01DbtrSts', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 868, 3), )

    
    DbtrSts = property(__DbtrSts.value, __DbtrSts.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}CertId uses Python identifier CertId
    __CertId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CertId'), 'CertId', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01CertId', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 869, 3), )

    
    CertId = property(__CertId.value, __CertId.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}FrmsCd uses Python identifier FrmsCd
    __FrmsCd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrmsCd'), 'FrmsCd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01FrmsCd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 870, 3), )

    
    FrmsCd = property(__FrmsCd.value, __FrmsCd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prd uses Python identifier Prd
    __Prd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prd'), 'Prd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01Prd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 871, 3), )

    
    Prd = property(__Prd.value, __Prd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxAmt uses Python identifier TaxAmt
    __TaxAmt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), 'TaxAmt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01TaxAmt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 872, 3), )

    
    TaxAmt = property(__TaxAmt.value, __TaxAmt.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}AddtlInf uses Python identifier AddtlInf
    __AddtlInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf'), 'AddtlInf', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecord2_urnCBIxsdCBIPaymentRequest_00_04_01AddtlInf', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 873, 3), )

    
    AddtlInf = property(__AddtlInf.value, __AddtlInf.set, None, None)

    _ElementMap.update({
        __Tp.name() : __Tp,
        __Ctgy.name() : __Ctgy,
        __CtgyDtls.name() : __CtgyDtls,
        __DbtrSts.name() : __DbtrSts,
        __CertId.name() : __CertId,
        __FrmsCd.name() : __FrmsCd,
        __Prd.name() : __Prd,
        __TaxAmt.name() : __TaxAmt,
        __AddtlInf.name() : __AddtlInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxRecord2 = TaxRecord2
Namespace.addCategoryObject('typeBinding', 'TaxRecord2', TaxRecord2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxRecordDetails2 with content type ELEMENT_ONLY
class TaxRecordDetails2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}TaxRecordDetails2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxRecordDetails2')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 876, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Prd uses Python identifier Prd
    __Prd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prd'), 'Prd', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecordDetails2_urnCBIxsdCBIPaymentRequest_00_04_01Prd', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 878, 3), )

    
    Prd = property(__Prd.value, __Prd.set, None, None)

    
    # Element {urn:CBI:xsd:CBIPaymentRequest.00.04.01}Amt uses Python identifier Amt
    __Amt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amt'), 'Amt', '__urnCBIxsdCBIPaymentRequest_00_04_01_TaxRecordDetails2_urnCBIxsdCBIPaymentRequest_00_04_01Amt', False, pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 879, 3), )

    
    Amt = property(__Amt.value, __Amt.set, None, None)

    _ElementMap.update({
        __Prd.name() : __Prd,
        __Amt.name() : __Amt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TaxRecordDetails2 = TaxRecordDetails2
Namespace.addCategoryObject('typeBinding', 'TaxRecordDetails2', TaxRecordDetails2)


# Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ActiveOrHistoricCurrencyAndAmount with content type SIMPLE
class ActiveOrHistoricCurrencyAndAmount (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:CBI:xsd:CBIPaymentRequest.00.04.01}ActiveOrHistoricCurrencyAndAmount with content type SIMPLE"""
    _TypeDefinition = CBIActiveOrHistoricCurrencyAndAmount_SimpleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActiveOrHistoricCurrencyAndAmount')
    _XSDLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 125, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is CBIActiveOrHistoricCurrencyAndAmount_SimpleType
    
    # Attribute Ccy uses Python identifier Ccy
    __Ccy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Ccy'), 'Ccy', '__urnCBIxsdCBIPaymentRequest_00_04_01_ActiveOrHistoricCurrencyAndAmount_Ccy', _module_typeBindings.ActiveOrHistoricCurrencyCode, required=True)
    __Ccy._DeclarationLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 128, 4)
    __Ccy._UseLocation = pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 128, 4)
    
    Ccy = property(__Ccy.value, __Ccy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Ccy.name() : __Ccy
    })
_module_typeBindings.ActiveOrHistoricCurrencyAndAmount = ActiveOrHistoricCurrencyAndAmount
Namespace.addCategoryObject('typeBinding', 'ActiveOrHistoricCurrencyAndAmount', ActiveOrHistoricCurrencyAndAmount)


CBIPaymentRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CBIPaymentRequest'), CBIPaymentRequest_00_04_01, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', CBIPaymentRequest.name().localName(), CBIPaymentRequest)



CBIPaymentRequest_00_04_01._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), CBIGroupHeader, scope=CBIPaymentRequest_00_04_01, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 9, 3)))

CBIPaymentRequest_00_04_01._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtInf'), CBIPaymentInstructionInformation, scope=CBIPaymentRequest_00_04_01, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 13, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentRequest_00_04_01._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 9, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPaymentRequest_00_04_01._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 13, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPaymentRequest_00_04_01._Automaton = _BuildAutomaton()




CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), Max35Text, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 18, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), ISODateTime, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 19, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), Max15NumericText, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 20, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), CBIDecimalNumber, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 21, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InitgPty'), CBIPartyIdentification1, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 22, 3)))

CBIGroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt'), CBIBranchAndFinancialInstitutionIdentification1, scope=CBIGroupHeader, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 23, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 23, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MsgId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 18, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 20, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 21, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InitgPty')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 22, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIGroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 23, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIGroupHeader._Automaton = _BuildAutomaton_()




CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId'), Max35Text, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 35, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd'), PaymentMethod3Code, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 36, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg'), BatchBookingIndicator, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 37, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), CBIPaymentTypeInformation1, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 38, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt'), DateAndDateTime2Choice, scope=CBIPaymentInstructionInformation, documentation=' CHAN: Type Changed into DateAndDateTime2Choice for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 39, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), CBIPartyIdentification4, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 44, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct'), CBICashAccount2, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 45, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt'), CBIBranchAndFinancialInstitutionIdentification2, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 46, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), CBIPartyIdentification2, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 47, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr'), CBIChargeBearerTypeCode, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 48, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct'), CBICashAccount1, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 49, 3)))

CBIPaymentInstructionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf'), CBICreditTransferTransactionInformation, scope=CBIPaymentInstructionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 50, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 37, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 38, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 47, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 48, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 49, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 35, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 36, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 37, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 38, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 39, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dbtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 44, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 45, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 46, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 47, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 48, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 49, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPaymentInstructionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 50, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPaymentInstructionInformation._Automaton = _BuildAutomaton_2()




CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtId'), PaymentIdentification1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 69, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), CBIPaymentTypeInformation2, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 70, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), CBIAmountType1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 71, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChqInstr'), CBICheque1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 72, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), CBIPartyIdentification2, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 73, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SrvInf'), CBISrvInf1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 74, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtrAgt'), CBIBranchAndFinancialInstitutionIdentification3, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 75, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), CBIPartyIdentification3, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 76, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtrAcct'), CBICashAccount3, scope=CBICreditTransferTransactionInformation, documentation=' CHAN - Type Changed in order to add the optional Proxy Field under Creditor Account ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 77, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtCdtr'), CBIPartyIdentification3, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 82, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrForCdtrAgt'), InstructionForCreditorAgent1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 83, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DestCdtrRsp'), CBIPartyIdentification5, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 84, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Purp'), Purpose1Choice, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 85, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgltryRptg'), CBIRegulatoryReporting1, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 86, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tax'), TaxInformation8, scope=CBICreditTransferTransactionInformation, documentation=' CHAN - Complex structure included for the migration to v2019 ISO message ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 87, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RltdRmtInf'), CBIRemittanceLocation1, scope=CBICreditTransferTransactionInformation, documentation=' CHAN - Modified structure to adopt v2019 ISO message ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 92, 3)))

CBICreditTransferTransactionInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtInf'), RemittanceInformation16, scope=CBICreditTransferTransactionInformation, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 97, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 70, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 72, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 73, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 74, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 75, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 77, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 82, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 83, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 84, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 85, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 86, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 87, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=10, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 92, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 97, 3))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 69, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 70, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 71, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChqInstr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 72, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 73, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SrvInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 74, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtrAgt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 75, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cdtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 76, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtrAcct')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 77, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtCdtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 82, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrForCdtrAgt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 83, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DestCdtrRsp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 84, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Purp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 85, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgltryRptg')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 86, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tax')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 87, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RltdRmtInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 92, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CBICreditTransferTransactionInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 97, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICreditTransferTransactionInformation._Automaton = _BuildAutomaton_3()




AddressType3Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), AddressType2Code, scope=AddressType3Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 121, 3)))

AddressType3Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), GenericIdentification30, scope=AddressType3Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 122, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressType3Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 121, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressType3Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 122, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddressType3Choice._Automaton = _BuildAutomaton_4()




CategoryPurpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalCategoryPurpose1Code, scope=CategoryPurpose1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 134, 12)))

CategoryPurpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CategoryPurpose1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 135, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CategoryPurpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 134, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CategoryPurpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 135, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CategoryPurpose1Choice._Automaton = _BuildAutomaton_5()




CBIAccountIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IBAN'), IBAN2007Identifier, scope=CBIAccountIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 140, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIAccountIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IBAN')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 140, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIAccountIdentification1._Automaton = _BuildAutomaton_6()




CBIAmountType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstdAmt'), ActiveOrHistoricCurrencyAndAmount, scope=CBIAmountType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 145, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIAmountType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstdAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 145, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIAmountType1._Automaton = _BuildAutomaton_7()




CBIBranchAndFinancialInstitutionIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), CBIFinancialInstitutionIdentification1, scope=CBIBranchAndFinancialInstitutionIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 150, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIBranchAndFinancialInstitutionIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 150, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIBranchAndFinancialInstitutionIdentification1._Automaton = _BuildAutomaton_8()




CBIBranchAndFinancialInstitutionIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), CBIFinancialInstitutionIdentification3, scope=CBIBranchAndFinancialInstitutionIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 155, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIBranchAndFinancialInstitutionIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 155, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIBranchAndFinancialInstitutionIdentification2._Automaton = _BuildAutomaton_9()




CBIBranchAndFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId'), CBIFinancialInstitutionIdentification2, scope=CBIBranchAndFinancialInstitutionIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 160, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIBranchAndFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FinInstnId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 160, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIBranchAndFinancialInstitutionIdentification3._Automaton = _BuildAutomaton_10()




CBICashAccount1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIAccountIdentification1, scope=CBICashAccount1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 165, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICashAccount1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 165, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICashAccount1._Automaton = _BuildAutomaton_11()




CBICashAccount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIAccountIdentification1, scope=CBICashAccount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 170, 3)))

CBICashAccount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), CashAccountType2Choice, scope=CBICashAccount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 171, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 171, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICashAccount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 170, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBICashAccount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 171, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICashAccount2._Automaton = _BuildAutomaton_12()




CBICashAccount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIAccountIdentification1, scope=CBICashAccount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 176, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBICashAccount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 176, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBICashAccount3._Automaton = _BuildAutomaton_13()




CashAccountType2Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalCashAccountType1Code, scope=CashAccountType2Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 181, 3)))

CashAccountType2Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CashAccountType2Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 182, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CashAccountType2Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 181, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CashAccountType2Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 182, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CashAccountType2Choice._Automaton = _BuildAutomaton_14()




CBICheque1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChqTp'), CBIChequeType1Code, scope=CBICheque1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 187, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 187, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBICheque1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChqTp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 187, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBICheque1._Automaton = _BuildAutomaton_15()




CBIClearingSystemMemberIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MmbId'), Max35Text, scope=CBIClearingSystemMemberIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 192, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIClearingSystemMemberIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MmbId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 192, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIClearingSystemMemberIdentification1._Automaton = _BuildAutomaton_16()




CBIFinancialInstitutionIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), CBIClearingSystemMemberIdentification1, scope=CBIFinancialInstitutionIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 197, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 197, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIFinancialInstitutionIdentification1._Automaton = _BuildAutomaton_17()




CBIFinancialInstitutionIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BICFI'), BICFIDec2014Identifier, scope=CBIFinancialInstitutionIdentification2, documentation=' CHAN: Name Changed into BICFI and Type Changed into BICFIDec2014Identifier for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 202, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BICFI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 202, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIFinancialInstitutionIdentification2._Automaton = _BuildAutomaton_18()




CBIFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BICFI'), BICFIDec2014Identifier, scope=CBIFinancialInstitutionIdentification3, documentation=' CHAN: Name Changed into BICFI and Type Changed into BICFIDec2014Identifier for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 211, 3)))

CBIFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId'), CBIClearingSystemMemberIdentification1, scope=CBIFinancialInstitutionIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 216, 3)))

CBIFinancialInstitutionIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=CBIFinancialInstitutionIdentification3, documentation=' CHAN: Field included for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 217, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 211, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 217, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BICFI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 211, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClrSysMmbId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 216, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIFinancialInstitutionIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 217, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIFinancialInstitutionIdentification3._Automaton = _BuildAutomaton_19()




CBIGenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=CBIGenericIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 226, 3)))

CBIGenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=CBIGenericIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 227, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 227, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 226, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 227, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIGenericIdentification1._Automaton = _BuildAutomaton_20()




CBIGenericIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=CBIGenericIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 232, 3)))

CBIGenericIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=CBIGenericIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 233, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 232, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIGenericIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 233, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIGenericIdentification2._Automaton = _BuildAutomaton_21()




CBIIdType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification1, scope=CBIIdType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 238, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIIdType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 238, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIIdType1._Automaton = _BuildAutomaton_22()




CBIIdType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification3, scope=CBIIdType2, documentation=' CHAN: Removed "OR" XSD check and restored "sequence" for ISO 20022 compliance ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 243, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIIdType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 243, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIIdType2._Automaton = _BuildAutomaton_23()




CBIIdType3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification4, scope=CBIIdType3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 252, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIIdType3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 252, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIIdType3._Automaton = _BuildAutomaton_24()




CBILocalInstrument1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CBILocalInstrument1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 257, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBILocalInstrument1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 257, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBILocalInstrument1._Automaton = _BuildAutomaton_25()




CBILocalInstrument2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalLocalInstrument1Code, scope=CBILocalInstrument2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 262, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBILocalInstrument2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 262, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBILocalInstrument2._Automaton = _BuildAutomaton_26()




CBIOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIOrganisationIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 267, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 267, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIOrganisationIdentification1._Automaton = _BuildAutomaton_27()




CBIOrganisationIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), AnyBICDec2014Identifier, scope=CBIOrganisationIdentification2, documentation=' CHAN: Name Changed into AnyBIC and Type Changed into AnyBICDec2014Identifier for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 272, 3)))

CBIOrganisationIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=CBIOrganisationIdentification2, documentation=' CHAN: Field included for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 277, 3)))

CBIOrganisationIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIOrganisationIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 282, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 272, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 277, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 282, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 272, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 277, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 282, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIOrganisationIdentification2._Automaton = _BuildAutomaton_28()




CBIOrganisationIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), AnyBICDec2014Identifier, scope=CBIOrganisationIdentification3, documentation=' CHAN: Name Changed into AnyBIC and Type Changed into AnyBICDec2014Identifier for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 287, 3)))

CBIOrganisationIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=CBIOrganisationIdentification3, documentation=' CHAN: Field included for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 292, 3)))

CBIOrganisationIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIOrganisationIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 297, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 287, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 292, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 297, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 287, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 292, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 297, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIOrganisationIdentification3._Automaton = _BuildAutomaton_29()




CBIOrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification2, scope=CBIOrganisationIdentification4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 302, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIOrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 302, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIOrganisationIdentification4._Automaton = _BuildAutomaton_30()




CBIParty1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), CBIOrganisationIdentification2, scope=CBIParty1Choice, documentation=' CHAN: Removed "OR" XSD check and restored "sequence" for ISO 20022 compliance ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 307, 3)))

CBIParty1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), CBIPersonIdentification1, scope=CBIParty1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 312, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIParty1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 307, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIParty1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvtId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 312, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIParty1Choice._Automaton = _BuildAutomaton_31()




CBIPartyIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 317, 3)))

CBIPartyIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType1, scope=CBIPartyIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 318, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 317, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 317, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 318, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification1._Automaton = _BuildAutomaton_32()




CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 323, 3)))

CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress24, scope=CBIPartyIdentification2, documentation=' CHAN: Type Changed into CBIPostalAddress24 for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 324, 3)))

CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType2, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 329, 3)))

CBIPartyIdentification2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=CBIPartyIdentification2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 330, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 323, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 324, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 329, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 330, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 323, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 324, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 329, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 330, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPartyIdentification2._Automaton = _BuildAutomaton_33()




CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 335, 3)))

CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress24, scope=CBIPartyIdentification3, documentation=' CHAN: Type Changed into CBIPostalAddress24 for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 336, 3)))

CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIParty1Choice, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 341, 3)))

CBIPartyIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=CBIPartyIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 342, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 336, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 341, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 342, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 335, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 336, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 341, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 342, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification3._Automaton = _BuildAutomaton_34()




CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 347, 3)))

CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), CBIPostalAddress24, scope=CBIPartyIdentification4, documentation=' CHAN: Type Changed into CBIPostalAddress24 for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 348, 3)))

CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType2, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 353, 3)))

CBIPartyIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=CBIPartyIdentification4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 354, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 348, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 353, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 354, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 347, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 348, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 353, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 354, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification4._Automaton = _BuildAutomaton_35()




CBIPartyIdentification5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=CBIPartyIdentification5, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 359, 3)))

CBIPartyIdentification5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), CBIIdType3, scope=CBIPartyIdentification5, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 360, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 360, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 359, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPartyIdentification5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 360, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPartyIdentification5._Automaton = _BuildAutomaton_36()




CBIPaymentTypeInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrPrty'), Priority2Code, scope=CBIPaymentTypeInformation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 365, 3)))

CBIPaymentTypeInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), CBIServiceLevel1, scope=CBIPaymentTypeInformation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 366, 3)))

CBIPaymentTypeInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm'), CBILocalInstrument2, scope=CBIPaymentTypeInformation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 367, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 365, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 366, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 367, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrPrty')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 365, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 366, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 367, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPaymentTypeInformation1._Automaton = _BuildAutomaton_37()




CBIPaymentTypeInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl'), CBIServiceLevel2, scope=CBIPaymentTypeInformation2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 372, 3)))

CBIPaymentTypeInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm'), CBILocalInstrument1, scope=CBIPaymentTypeInformation2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 373, 3)))

CBIPaymentTypeInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtgyPurp'), CategoryPurpose1Choice, scope=CBIPaymentTypeInformation2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 374, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 372, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 373, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 374, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SvcLvl')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 372, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LclInstrm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 373, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPaymentTypeInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtgyPurp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 374, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPaymentTypeInformation2._Automaton = _BuildAutomaton_38()




CBIPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), CBIGenericIdentification1, scope=CBIPersonIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 379, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 379, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIPersonIdentification1._Automaton = _BuildAutomaton_39()




CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdrTp'), AddressType3Choice, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 384, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dept'), Max70Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 385, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubDept'), Max70Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 386, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), Max70Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 387, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BldgNb'), Max16Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 388, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BldgNm'), Max35Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 389, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Flr'), Max70Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 390, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstBx'), Max16Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 391, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Room'), Max70Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 392, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstCd'), Max16Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 393, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), Max35Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 394, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TwnLctnNm'), Max35Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 395, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm'), Max35Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 396, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn'), Max35Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 397, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 398, 3)))

CBIPostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdrLine'), Max70Text, scope=CBIPostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 399, 3)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 384, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 385, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 386, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 387, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 388, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 389, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 390, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 391, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 392, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 393, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 394, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 395, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 396, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 397, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 398, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 399, 3))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdrTp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 384, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dept')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 385, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubDept')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 386, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrtNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 387, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BldgNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 388, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BldgNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 389, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Flr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 390, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstBx')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 391, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Room')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 392, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstCd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 393, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TwnNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 394, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TwnLctnNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 395, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 396, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 397, 3))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 398, 3))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CBIPostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdrLine')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 399, 3))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIPostalAddress24._Automaton = _BuildAutomaton_40()




CBIRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtCdtRptgInd'), CBIRegulatoryReportingType1Code, scope=CBIRegulatoryReporting1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 404, 3)))

CBIRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dtls'), CBIStructuredRegulatoryReporting1, scope=CBIRegulatoryReporting1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 405, 3)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 405, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtCdtRptgInd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 404, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dtls')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 405, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIRegulatoryReporting1._Automaton = _BuildAutomaton_41()




CBIRemittanceLocation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtId'), Max35Text, scope=CBIRemittanceLocation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 410, 3)))

CBIRemittanceLocation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnDtls'), CBIRemittanceLocationData1, scope=CBIRemittanceLocation1, documentation=' CHAN: Element included for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 411, 3)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 410, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 411, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 410, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtLctnDtls')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 411, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CBIRemittanceLocation1._Automaton = _BuildAutomaton_42()




CBIRemittanceLocationData1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mtd'), CBIRemittanceLocationMethod1Code, scope=CBIRemittanceLocationData1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 420, 3)))

CBIRemittanceLocationData1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElctrncAdr'), Max2048Text, scope=CBIRemittanceLocationData1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 421, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 421, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocationData1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mtd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 420, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIRemittanceLocationData1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ElctrncAdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 421, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIRemittanceLocationData1._Automaton = _BuildAutomaton_43()




CBIServiceLevel1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), CBIServiceLevel1Code, scope=CBIServiceLevel1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 426, 3)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIServiceLevel1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 426, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIServiceLevel1._Automaton = _BuildAutomaton_44()




CBIServiceLevel2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CBIServiceLevel2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 431, 3)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIServiceLevel2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 431, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIServiceLevel2._Automaton = _BuildAutomaton_45()




CBIStructuredRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), STD_ANON, scope=CBIStructuredRegulatoryReporting1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 436, 3)))

CBIStructuredRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=CBIStructuredRegulatoryReporting1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 445, 3)))

CBIStructuredRegulatoryReporting1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Inf'), Max35Text, scope=CBIStructuredRegulatoryReporting1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 446, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 445, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 446, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CBIStructuredRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 436, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CBIStructuredRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 445, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CBIStructuredRegulatoryReporting1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Inf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 446, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CBIStructuredRegulatoryReporting1._Automaton = _BuildAutomaton_46()




CreditorReferenceInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), CreditorReferenceType2, scope=CreditorReferenceInformation2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 451, 3)))

CreditorReferenceInformation2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ref'), Max35Text, scope=CreditorReferenceInformation2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 452, 3)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 451, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 452, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 451, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceInformation2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ref')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 452, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CreditorReferenceInformation2._Automaton = _BuildAutomaton_47()




CreditorReferenceType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), DocumentType3Code, scope=CreditorReferenceType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 458, 4)))

CreditorReferenceType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=CreditorReferenceType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 459, 4)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 458, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 459, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreditorReferenceType1Choice._Automaton = _BuildAutomaton_48()




CreditorReferenceType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), CreditorReferenceType1Choice, scope=CreditorReferenceType2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 465, 3)))

CreditorReferenceType2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=CreditorReferenceType2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 466, 3)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 466, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 465, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CreditorReferenceType2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 466, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CreditorReferenceType2._Automaton = _BuildAutomaton_49()




DateAndPlaceOfBirth1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BirthDt'), ISODate, scope=DateAndPlaceOfBirth1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 471, 3)))

DateAndPlaceOfBirth1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth'), Max35Text, scope=DateAndPlaceOfBirth1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 472, 3)))

DateAndPlaceOfBirth1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth'), Max35Text, scope=DateAndPlaceOfBirth1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 473, 3)))

DateAndPlaceOfBirth1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth'), CountryCode, scope=DateAndPlaceOfBirth1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 474, 3)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 472, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BirthDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 471, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 472, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 473, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateAndPlaceOfBirth1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 474, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateAndPlaceOfBirth1._Automaton = _BuildAutomaton_50()




DateAndDateTime2Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dt'), ISODate, scope=DateAndDateTime2Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 479, 3)))

DateAndDateTime2Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DtTm'), ISODateTime, scope=DateAndDateTime2Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 480, 3)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateAndDateTime2Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 479, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateAndDateTime2Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DtTm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 480, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateAndDateTime2Choice._Automaton = _BuildAutomaton_51()




DatePeriod2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrDt'), ISODate, scope=DatePeriod2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 485, 3)))

DatePeriod2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ToDt'), ISODate, scope=DatePeriod2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 486, 3)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DatePeriod2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 485, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DatePeriod2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ToDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 486, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DatePeriod2._Automaton = _BuildAutomaton_52()




DiscountAmountAndType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), DiscountAmountType1Choice, scope=DiscountAmountAndType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 491, 3)))

DiscountAmountAndType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=DiscountAmountAndType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 492, 3)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 491, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DiscountAmountAndType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 491, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DiscountAmountAndType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 492, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DiscountAmountAndType1._Automaton = _BuildAutomaton_53()




DiscountAmountType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalDiscountAmountType1Code, scope=DiscountAmountType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 497, 3)))

DiscountAmountType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=DiscountAmountType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 498, 3)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DiscountAmountType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 497, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DiscountAmountType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 498, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DiscountAmountType1Choice._Automaton = _BuildAutomaton_54()




DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 503, 3)))

DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtDbtInd'), CreditDebitCode, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 504, 3)))

DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rsn'), Max4Text, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 505, 3)))

DocumentAdjustment1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf'), Max140Text, scope=DocumentAdjustment1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 506, 3)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 504, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 505, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 506, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 503, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtDbtInd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 504, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rsn')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 505, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DocumentAdjustment1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 506, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentAdjustment1._Automaton = _BuildAutomaton_55()




DocumentLineIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), DocumentLineType1, scope=DocumentLineIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 511, 3)))

DocumentLineIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nb'), Max35Text, scope=DocumentLineIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 512, 3)))

DocumentLineIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RltdDt'), ISODate, scope=DocumentLineIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 513, 3)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 511, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 512, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 513, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentLineIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 511, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DocumentLineIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 512, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DocumentLineIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RltdDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 513, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DocumentLineIdentification1._Automaton = _BuildAutomaton_56()




DocumentLineInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), DocumentLineIdentification1, scope=DocumentLineInformation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 518, 3)))

DocumentLineInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Desc'), Max2048Text, scope=DocumentLineInformation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 519, 3)))

DocumentLineInformation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), RemittanceAmount3, scope=DocumentLineInformation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 520, 3)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 519, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 520, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentLineInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 518, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentLineInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Desc')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 519, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DocumentLineInformation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 520, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentLineInformation1._Automaton = _BuildAutomaton_57()




DocumentLineType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), DocumentLineType1Choice, scope=DocumentLineType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 525, 3)))

DocumentLineType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=DocumentLineType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 526, 3)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 526, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentLineType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 525, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DocumentLineType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 526, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentLineType1._Automaton = _BuildAutomaton_58()




DocumentLineType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalDocumentLineType1Code, scope=DocumentLineType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 531, 3)))

DocumentLineType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=DocumentLineType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 532, 3)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentLineType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 531, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DocumentLineType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 532, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DocumentLineType1Choice._Automaton = _BuildAutomaton_59()




Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), GarnishmentType1, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 537, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Grnshee'), PartyIdentification135, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 538, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GrnshmtAdmstr'), PartyIdentification135, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 539, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RefNb'), Max140Text, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 540, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dt'), ISODate, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 541, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), ActiveOrHistoricCurrencyAndAmount, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 542, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FmlyMdclInsrncInd'), TrueFalseIndicator, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 543, 3)))

Garnishment3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MplyeeTermntnInd'), TrueFalseIndicator, scope=Garnishment3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 544, 3)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 538, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 539, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 540, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 541, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 542, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 543, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 544, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 537, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Grnshee')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 538, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GrnshmtAdmstr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 539, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RefNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 540, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 541, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 542, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FmlyMdclInsrncInd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 543, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Garnishment3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MplyeeTermntnInd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 544, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Garnishment3._Automaton = _BuildAutomaton_60()




GarnishmentType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), GarnishmentType1Choice, scope=GarnishmentType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 549, 3)))

GarnishmentType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GarnishmentType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 550, 3)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 550, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GarnishmentType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 549, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GarnishmentType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 550, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GarnishmentType1._Automaton = _BuildAutomaton_61()




GarnishmentType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalGarnishmentType1Code, scope=GarnishmentType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 555, 3)))

GarnishmentType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=GarnishmentType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 556, 3)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GarnishmentType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 555, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GarnishmentType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 556, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GarnishmentType1Choice._Automaton = _BuildAutomaton_62()




GenericIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 561, 3)))

GenericIdentification3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericIdentification3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 562, 3)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 562, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 561, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericIdentification3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 562, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericIdentification3._Automaton = _BuildAutomaton_63()




GenericIdentification30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Exact4AlphaNumericText, scope=GenericIdentification30, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 567, 3)))

GenericIdentification30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericIdentification30, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 568, 3)))

GenericIdentification30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), Max35Text, scope=GenericIdentification30, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 569, 3)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 569, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericIdentification30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 567, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericIdentification30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 568, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericIdentification30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 569, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericIdentification30._Automaton = _BuildAutomaton_64()




GenericOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericOrganisationIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 574, 3)))

GenericOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), OrganisationIdentificationSchemeName1Choice, scope=GenericOrganisationIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 575, 3)))

GenericOrganisationIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericOrganisationIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 576, 3)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 575, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 576, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 574, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 575, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenericOrganisationIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 576, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericOrganisationIdentification1._Automaton = _BuildAutomaton_65()




GenericPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericPersonIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 581, 3)))

GenericPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), PersonIdentificationSchemeName1Choice, scope=GenericPersonIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 582, 3)))

GenericPersonIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericPersonIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 583, 3)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 582, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 583, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 581, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 582, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenericPersonIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 583, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericPersonIdentification1._Automaton = _BuildAutomaton_66()




OrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), AnyBICDec2014Identifier, scope=OrganisationIdentification4, documentation=' CHAN: Name Changed into AnyBIC and Type Changed into AnyBICDec2014Identifier for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 588, 3)))

OrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=OrganisationIdentification4, documentation=' CHAN: Field included for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 593, 3)))

OrganisationIdentification4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), GenericOrganisationIdentification1, scope=OrganisationIdentification4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 598, 3)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 588, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 593, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 598, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 588, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 593, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 598, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrganisationIdentification4._Automaton = _BuildAutomaton_67()




OrganisationIdentification29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC'), AnyBICDec2014Identifier, scope=OrganisationIdentification29, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 603, 3)))

OrganisationIdentification29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LEI'), LEIIdentifier, scope=OrganisationIdentification29, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 604, 3)))

OrganisationIdentification29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), GenericOrganisationIdentification1, scope=OrganisationIdentification29, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 605, 3)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 603, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 604, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 605, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AnyBIC')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 603, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LEI')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 604, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentification29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 605, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrganisationIdentification29._Automaton = _BuildAutomaton_68()




OrganisationIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalOrganisationIdentification1Code, scope=OrganisationIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 611, 4)))

OrganisationIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=OrganisationIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 612, 4)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 611, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganisationIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 612, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrganisationIdentificationSchemeName1Choice._Automaton = _BuildAutomaton_69()




OtherContact1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChanlTp'), Max4Text, scope=OtherContact1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 618, 3)))

OtherContact1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max128Text, scope=OtherContact1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 619, 3)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 619, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OtherContact1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChanlTp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 618, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OtherContact1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 619, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OtherContact1._Automaton = _BuildAutomaton_70()




PartyIdentification135._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max140Text, scope=PartyIdentification135, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 624, 3)))

PartyIdentification135._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr'), PostalAddress24, scope=PartyIdentification135, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 625, 3)))

PartyIdentification135._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Party38Choice, scope=PartyIdentification135, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 626, 3)))

PartyIdentification135._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes'), CountryCode, scope=PartyIdentification135, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 627, 3)))

PartyIdentification135._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls'), Contact4, scope=PartyIdentification135, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 628, 3)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 624, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 625, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 626, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 627, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 628, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification135._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 624, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification135._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstlAdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 625, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification135._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 626, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification135._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfRes')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 627, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PartyIdentification135._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 628, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PartyIdentification135._Automaton = _BuildAutomaton_71()




Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NmPrfx'), NamePrefix2Code, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 633, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max140Text, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 634, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PhneNb'), PhoneNumber, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 635, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MobNb'), PhoneNumber, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 636, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FaxNb'), PhoneNumber, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 637, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmailAdr'), Max2048Text, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 638, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmailPurp'), Max35Text, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 639, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JobTitl'), Max35Text, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 640, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rspnsblty'), Max35Text, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 641, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dept'), Max70Text, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 642, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), OtherContact1, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 643, 3)))

Contact4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrefrdMtd'), PreferredContactMethod1Code, scope=Contact4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 644, 3)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 633, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 634, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 635, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 636, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 637, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 638, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 639, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 640, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 641, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 642, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 643, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 644, 3))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NmPrfx')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 633, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 634, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PhneNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 635, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MobNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 636, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FaxNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 637, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmailAdr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 638, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmailPurp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 639, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JobTitl')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 640, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rspnsblty')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 641, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dept')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 642, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 643, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Contact4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrefrdMtd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 644, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Contact4._Automaton = _BuildAutomaton_72()




Party38Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), OrganisationIdentification29, scope=Party38Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 649, 3)))

Party38Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), PersonIdentification13, scope=Party38Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 650, 3)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party38Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 649, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Party38Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvtId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 650, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Party38Choice._Automaton = _BuildAutomaton_73()




PaymentIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrId'), Max35Text, scope=PaymentIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 655, 3)))

PaymentIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndToEndId'), Max35Text, scope=PaymentIdentification1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 656, 3)))

PaymentIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UETR'), UUIDv4Identifier, scope=PaymentIdentification1, documentation=' CHAN: Field included for v2019 ISO message migration ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 657, 3)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 657, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PaymentIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 655, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PaymentIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndToEndId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 656, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PaymentIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UETR')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 657, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PaymentIdentification1._Automaton = _BuildAutomaton_74()




PersonIdentification13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth'), DateAndPlaceOfBirth1, scope=PersonIdentification13, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 666, 3)))

PersonIdentification13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), GenericPersonIdentification1, scope=PersonIdentification13, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 667, 3)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 666, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 667, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonIdentification13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 666, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonIdentification13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 667, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonIdentification13._Automaton = _BuildAutomaton_75()




PersonIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalPersonIdentification1Code, scope=PersonIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 673, 4)))

PersonIdentificationSchemeName1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=PersonIdentificationSchemeName1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 674, 4)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 673, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PersonIdentificationSchemeName1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 674, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PersonIdentificationSchemeName1Choice._Automaton = _BuildAutomaton_76()




PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdrTp'), AddressType3Choice, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 680, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dept'), Max70Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 681, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubDept'), Max70Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 682, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), Max70Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 683, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BldgNb'), Max16Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 684, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BldgNm'), Max35Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 685, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Flr'), Max70Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 686, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstBx'), Max16Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 687, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Room'), Max70Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 688, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstCd'), Max16Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 689, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), Max35Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 690, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TwnLctnNm'), Max35Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 691, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm'), Max35Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 692, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn'), Max35Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 693, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 694, 3)))

PostalAddress24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdrLine'), Max70Text, scope=PostalAddress24, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 695, 3)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 680, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 681, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 682, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 683, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 684, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 685, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 686, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 687, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 688, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 689, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 690, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 691, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 692, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 693, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 694, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=7, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 695, 3))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdrTp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 680, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dept')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 681, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubDept')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 682, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrtNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 683, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BldgNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 684, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BldgNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 685, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Flr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 686, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstBx')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 687, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Room')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 688, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstCd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 689, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TwnNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 690, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TwnLctnNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 691, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 692, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrySubDvsn')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 693, 3))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 694, 3))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(PostalAddress24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdrLine')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 695, 3))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PostalAddress24._Automaton = _BuildAutomaton_77()




InstructionForCreditorAgent1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), Instruction3Code, scope=InstructionForCreditorAgent1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 700, 3)))

InstructionForCreditorAgent1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstrInf'), Max140Text, scope=InstructionForCreditorAgent1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 701, 3)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 700, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 701, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InstructionForCreditorAgent1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 700, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InstructionForCreditorAgent1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstrInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 701, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InstructionForCreditorAgent1._Automaton = _BuildAutomaton_78()




Purpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalPurpose1Code, scope=Purpose1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 707, 4)))

Purpose1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=Purpose1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 708, 4)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Purpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 707, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Purpose1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 708, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Purpose1Choice._Automaton = _BuildAutomaton_79()




RemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ustrd'), Max140Text, scope=RemittanceInformation16, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 714, 3)))

RemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Strd'), StructuredRemittanceInformation16, scope=RemittanceInformation16, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 715, 3)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 714, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 715, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ustrd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 714, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Strd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 715, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RemittanceInformation16._Automaton = _BuildAutomaton_80()




ReferredDocumentInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), ReferredDocumentType4, scope=ReferredDocumentInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 720, 3)))

ReferredDocumentInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nb'), Max35Text, scope=ReferredDocumentInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 721, 3)))

ReferredDocumentInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RltdDt'), ISODate, scope=ReferredDocumentInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 722, 3)))

ReferredDocumentInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LineDtls'), DocumentLineInformation1, scope=ReferredDocumentInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 723, 3)))

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 720, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 721, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 722, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 723, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 720, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 721, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RltdDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 722, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineDtls')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 723, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReferredDocumentInformation7._Automaton = _BuildAutomaton_81()




ReferredDocumentType3Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), DocumentType6Code, scope=ReferredDocumentType3Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 728, 3)))

ReferredDocumentType3Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=ReferredDocumentType3Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 729, 3)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType3Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 728, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType3Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 729, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferredDocumentType3Choice._Automaton = _BuildAutomaton_82()




ReferredDocumentType4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry'), ReferredDocumentType3Choice, scope=ReferredDocumentType4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 734, 3)))

ReferredDocumentType4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=ReferredDocumentType4, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 735, 3)))

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 735, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdOrPrtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 734, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferredDocumentType4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 735, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferredDocumentType4._Automaton = _BuildAutomaton_83()




RemittanceAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 740, 3)))

RemittanceAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt'), DiscountAmountAndType1, scope=RemittanceAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 741, 3)))

RemittanceAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 742, 3)))

RemittanceAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), TaxAmountAndType1, scope=RemittanceAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 743, 3)))

RemittanceAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn'), DocumentAdjustment1, scope=RemittanceAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 744, 3)))

RemittanceAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 745, 3)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 740, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 741, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 742, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 743, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 744, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 745, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 740, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 741, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 742, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 743, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 744, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 745, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RemittanceAmount2._Automaton = _BuildAutomaton_84()




RemittanceAmount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 750, 3)))

RemittanceAmount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt'), DiscountAmountAndType1, scope=RemittanceAmount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 751, 3)))

RemittanceAmount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 752, 3)))

RemittanceAmount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), TaxAmountAndType1, scope=RemittanceAmount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 753, 3)))

RemittanceAmount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn'), DocumentAdjustment1, scope=RemittanceAmount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 754, 3)))

RemittanceAmount3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt'), ActiveOrHistoricCurrencyAndAmount, scope=RemittanceAmount3, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 755, 3)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 750, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 751, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 752, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 753, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 754, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 755, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuePyblAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 750, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DscntApldAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 751, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtNoteAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 752, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 753, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdjstmntAmtAndRsn')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 754, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RemittanceAmount3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RmtdAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 755, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RemittanceAmount3._Automaton = _BuildAutomaton_85()




StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocInf'), ReferredDocumentInformation7, scope=StructuredRemittanceInformation16, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 760, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocAmt'), RemittanceAmount2, scope=StructuredRemittanceInformation16, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 761, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtrRefInf'), CreditorReferenceInformation2, scope=StructuredRemittanceInformation16, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 762, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Invcr'), PartyIdentification135, scope=StructuredRemittanceInformation16, documentation=' CHAN: Changed data type for migration to v2019 ISO Message ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 763, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Invcee'), PartyIdentification135, scope=StructuredRemittanceInformation16, documentation=' CHAN: Changed data type for migration to v2019 ISO Message ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 768, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxRmt'), TaxInformation7, scope=StructuredRemittanceInformation16, documentation=' CHAN - Complex structure included for the migration to v2019 ISO message ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 773, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GrnshmtRmt'), Garnishment3, scope=StructuredRemittanceInformation16, documentation=' CHAN - Complex structure included for the migration to v2019 ISO message ', location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 778, 3)))

StructuredRemittanceInformation16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddtlRmtInf'), Max140Text, scope=StructuredRemittanceInformation16, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 783, 3)))

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 760, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 761, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 762, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 763, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 768, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 773, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 778, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=3, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 783, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 760, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RfrdDocAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 761, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtrRefInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 762, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Invcr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 763, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Invcee')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 768, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxRmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 773, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GrnshmtRmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 778, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(StructuredRemittanceInformation16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddtlRmtInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 783, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StructuredRemittanceInformation16._Automaton = _BuildAutomaton_86()




TaxAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rate'), PercentageRate, scope=TaxAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 788, 3)))

TaxAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxblBaseAmt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 789, 3)))

TaxAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlAmt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 790, 3)))

TaxAmount2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dtls'), TaxRecordDetails2, scope=TaxAmount2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 791, 3)))

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 788, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 789, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 790, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 791, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rate')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 788, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxblBaseAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 789, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 790, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TaxAmount2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dtls')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 791, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxAmount2._Automaton = _BuildAutomaton_87()




TaxAmountAndType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), TaxAmountType1Choice, scope=TaxAmountAndType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 796, 3)))

TaxAmountAndType1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxAmountAndType1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 797, 3)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 796, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxAmountAndType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 796, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxAmountAndType1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 797, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxAmountAndType1._Automaton = _BuildAutomaton_88()




TaxAmountType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cd'), ExternalTaxAmountType1Code, scope=TaxAmountType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 802, 3)))

TaxAmountType1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prtry'), Max35Text, scope=TaxAmountType1Choice, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 803, 3)))

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxAmountType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 802, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxAmountType1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prtry')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 803, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxAmountType1Choice._Automaton = _BuildAutomaton_89()




TaxAuthorisation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Titl'), Max35Text, scope=TaxAuthorisation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 808, 3)))

TaxAuthorisation1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max140Text, scope=TaxAuthorisation1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 809, 3)))

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 808, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 809, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxAuthorisation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Titl')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 808, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxAuthorisation1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 809, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxAuthorisation1._Automaton = _BuildAutomaton_90()




TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), TaxParty1, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 814, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), TaxParty2, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 815, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), TaxParty2, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 816, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdmstnZone'), Max35Text, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 817, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RefNb'), Max140Text, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 818, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mtd'), Max35Text, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 819, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxblBaseAmt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 820, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxAmt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 821, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dt'), ISODate, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 822, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SeqNb'), Number, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 823, 3)))

TaxInformation7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rcrd'), TaxRecord2, scope=TaxInformation7, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 824, 3)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 814, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 815, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 816, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 817, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 818, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 819, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 820, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 821, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 822, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 823, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 824, 3))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cdtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 814, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dbtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 815, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 816, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdmstnZone')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 817, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RefNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 818, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mtd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 819, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxblBaseAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 820, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 821, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 822, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SeqNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 823, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rcrd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 824, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxInformation7._Automaton = _BuildAutomaton_91()




TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cdtr'), TaxParty1, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 829, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), TaxParty2, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 830, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdmstnZone'), Max35Text, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 831, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RefNb'), Max140Text, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 832, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mtd'), Max35Text, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 833, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxblBaseAmt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 834, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxAmt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 835, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dt'), ISODate, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 836, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SeqNb'), Number, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 837, 3)))

TaxInformation8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rcrd'), TaxRecord2, scope=TaxInformation8, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 838, 3)))

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 829, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 830, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 831, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 832, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 833, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 834, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 835, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 836, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 837, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 838, 3))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cdtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 829, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dbtr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 830, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdmstnZone')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 831, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RefNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 832, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mtd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 833, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxblBaseAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 834, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TtlTaxAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 835, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 836, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SeqNb')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 837, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(TaxInformation8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rcrd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 838, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxInformation8._Automaton = _BuildAutomaton_92()




TaxParty1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxId'), Max35Text, scope=TaxParty1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 843, 3)))

TaxParty1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegnId'), Max35Text, scope=TaxParty1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 844, 3)))

TaxParty1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxTp'), Max35Text, scope=TaxParty1, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 845, 3)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 843, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 844, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 845, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 843, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RegnId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 844, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxTp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 845, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxParty1._Automaton = _BuildAutomaton_93()




TaxParty2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxId'), Max35Text, scope=TaxParty2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 850, 3)))

TaxParty2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegnId'), Max35Text, scope=TaxParty2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 851, 3)))

TaxParty2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxTp'), Max35Text, scope=TaxParty2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 852, 3)))

TaxParty2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Authstn'), TaxAuthorisation1, scope=TaxParty2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 853, 3)))

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 850, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 851, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 852, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 853, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 850, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RegnId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 851, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxTp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 852, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TaxParty2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Authstn')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 853, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxParty2._Automaton = _BuildAutomaton_94()




TaxPeriod2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Yr'), ISODate, scope=TaxPeriod2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 858, 3)))

TaxPeriod2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), TaxRecordPeriod1Code, scope=TaxPeriod2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 859, 3)))

TaxPeriod2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrToDt'), DatePeriod2, scope=TaxPeriod2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 860, 3)))

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 858, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 859, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 860, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxPeriod2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Yr')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 858, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxPeriod2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 859, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxPeriod2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrToDt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 860, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxPeriod2._Automaton = _BuildAutomaton_95()




TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tp'), Max35Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 865, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctgy'), Max35Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 866, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtgyDtls'), Max35Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 867, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrSts'), Max35Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 868, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CertId'), Max35Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 869, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrmsCd'), Max35Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 870, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prd'), TaxPeriod2, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 871, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt'), TaxAmount2, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 872, 3)))

TaxRecord2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf'), Max140Text, scope=TaxRecord2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 873, 3)))

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 865, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 866, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 867, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 868, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 869, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 870, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 871, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 872, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 873, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tp')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 865, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctgy')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 866, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtgyDtls')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 867, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrSts')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 868, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CertId')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 869, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrmsCd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 870, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 871, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaxAmt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 872, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TaxRecord2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddtlInf')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 873, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxRecord2._Automaton = _BuildAutomaton_96()




TaxRecordDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prd'), TaxPeriod2, scope=TaxRecordDetails2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 878, 3)))

TaxRecordDetails2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amt'), ActiveOrHistoricCurrencyAndAmount, scope=TaxRecordDetails2, location=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 879, 3)))

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 878, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxRecordDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prd')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 878, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxRecordDetails2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amt')), pyxb.utils.utility.Location('/home/yamil/Downloads/CBIPaymentRequest.00.04.01.xsd', 879, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxRecordDetails2._Automaton = _BuildAutomaton_97()

