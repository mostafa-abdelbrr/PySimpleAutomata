from unittest import TestCase
import unittest
import DFA
import automata_IO


class TestRunAcceptance(TestCase):
    def setUp(self):
        self.dfa_run_acceptance_test_01 = automata_IO.dfa_dot_importer('./dot/dfa_run_acceptance_test_01.dot')

    # def tearDown(self):
    #     self.dfa = automata_IO.dfa_json_importer('./dot/dfa_run_acceptance_test_01.dot')

    def test_run_acceptance(self):
        """ Tests a correct run """
        self.assertEqual(
            DFA.run_acceptance(self.dfa_run_acceptance_test_01, ['s0', 's1', 's3', 's0'], ['5c', '10c', 'gum']), True)

    def test_run_acceptance_false(self):
        """ Tests a non correct run, good alphabet"""
        self.assertFalse(DFA.run_acceptance(self.dfa_run_acceptance_test_01, ['s0', 's1', 's3'], ['5c', '10c']))

    def test_run_acceptance_wrong_alphabet(self):
        """ Tests a non correct run with letters not present in the alphabet"""
        self.assertFalse(
            DFA.run_acceptance(self.dfa_run_acceptance_test_01, ['s0', 's1', 's3', 's0'], ['5c', '10c', 'wrong']))

    def test_run_acceptance_wrong_states(self):
        """ Tests a non correct run with states not present in the dfa"""
        self.assertFalse(
            DFA.run_acceptance(self.dfa_run_acceptance_test_01, ['s0', 's1', 'fake', 's0'], ['5c', '10c', 'gum']))

    @unittest.expectedFailure
    def test_run_acceptance_test_expected_failure(self):
        self.assertTrue(DFA.run_acceptance(self.dfa_run_acceptance_test_01, ['s0', 's1', 's3'], ['5c', '10c']))


class TestWordAcceptance(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    def test_word_acceptance(self):
        self.assertEqual(DFA.word_acceptance(self.dfa, ['5c', '10c', 'gum', '5c', '10c', 'gum']), True)


class TestDfaCompletion(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    @unittest.skip("TestDfaCompletion TODO")
    def test_dfa_completion(self):
        self.fail()


class TestDfaComplementation(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    @unittest.skip("TestDfaComplementation TODO")
    def test_dfa_complementation(self):
        self.fail()


class TestDfaIntersection(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    @unittest.skip("TestDfaIntersection TODO")
    def test_dfa_intersection(self):
        self.fail()


class TestDfaUnion(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    @unittest.skip("TestDfaUnion TODO")
    def test_dfa_union(self):
        self.fail()


class TestDfaMinimization(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    @unittest.skip("TestDfaMinimization TODO")
    def test_dfa_minimization(self):
        self.fail()


class TestDfaReachable(TestCase):
    def setUp(self):
        self.dfa = automata_IO.dfa_json_importer('../json/dfa_test.json')
        self.dfa_2 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')
        self.dfa_3 = automata_IO.dfa_json_importer('../json/dfa_f03_ai.json')

    @unittest.skip("TestDfaIntersection TODO")
    def test_dfa_reachable(self):
        self.fail()
