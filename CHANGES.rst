Changes
=======

0.3.3 (2020-02-05)
------------------

* Fixed installation issue on some Windows machines.

0.3.2 (2020-01-28)
------------------

* Improved Korean and Japanese currency detection.
* Declare Python 3.8 support.

0.3.1 (2019-10-21)
------------------

* Redundant $ signs are no longer returned as a part of currency, e.g.
  for ``SGD$ 100`` currency would be ``SGD``, not ``SGD$``.

0.3.0 (2019-10-19)
------------------

* New ``Price.fromstring`` argument ``decimal_separator`` allows to override
  decimal separator for the cases where it is known
  (i.e. disable decimal separator detection);
* NTD and RBM unofficial currency names are added;
* quantifiers in regular expressions are made non-greedy, which provides
  a small speedup;
* test improvements.

0.2.4 (2019-07-03)
------------------

* Declare price-parser as providing type annotations (pep-561). This enables
  better type checking for projects using price-parser.
* improved test coverage

0.2.3 (2019-06-18)
------------------

* Follow-up for 0.2.2 release: improved parsing of prices with 4+ digits
  after a decimal separator.

0.2.2 (2019-06-18)
------------------

* Fixed parsing of prices with 4+ digits after a decimal separator.

0.2.1 (2019-04-19)
------------------

* 23 additional currency symbols are added;
* ``A$`` alias for Australian Dollar is added.

0.2 (2019-04-12)
----------------

Added support for currencies replaced by euro.

0.1.1 (2019-04-12)
------------------

Minor packaging fixes.

0.1 (2019-04-12)
----------------

Initial release.