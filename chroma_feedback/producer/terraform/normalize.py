from typing import Any, Dict


def normalize_data(project : Dict[str, Any]) -> Dict[str, Any]:
	return\
	{
		'producer': 'terraform',
		'slug': project['id'],
		'active': True,
		'status': normalize_status(project['status'].lower()),
		'effect': normalize_effect(project['status'].lower())
	}


def normalize_status(status : str) -> str:
	statuses = {
		# Statuses with a '*' require manual intervention in TFE.
		'pending': 'process',				# Not running yet
		'plan-queued': 'process',			# Waiting to plan
		'planning': 'process',				# Checking infrastructure
		'canceled': 'failed',				# Run was cancelled
		'discarded': 'errored',				# Plan finished but was not applied
		'planned': 'process',				# Plan succeeded, needs approval *
		'planned-and-finished': 'passed',	# No changes, infrastructure OK
		'none': 'passed',					# Never run
		'cost-estimating': 'process',		# If you have it, TF estimates cost
		'cost-estimated': 'process', 		# of infrastructure.  Automatic...
		'policy-checking': 'process',		# Sentinel policies are run
		'policy-soft-failed': 'process', 	# A soft failure can be approved *
		'policy-override': 'process', 		# Applying over soft-fail policy
		'policy-checked': 'process', 		# Automatic, proceed to pre-apply
		'confirmed': 'process',				# Plan was confirmed, apply is next
		'apply-queued': 'process',			# Waiting to apply
		'applying': 'process',				# Apply in process
		'errored': 'failed',				# Apply had an error
		'applied': 'passed'					# Apply successful
	}

	return statuses.get(status, 'passed')

def normalize_effect(status : str) -> str:
	effects = {
		'planned': 'pulse',
		'policy-soft-failed': 'pulse'
	}

	return effects.get(status, 'default')
