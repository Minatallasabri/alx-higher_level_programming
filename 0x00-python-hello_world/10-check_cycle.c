#include "lists.h"

/**
 * check_cycle - function checks a cycle in list
 * @li: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *li)
{
	listint_t *curre, *chec;

	if (li == NULL || li->next == NULL)
		return (0);
	curre = li;
	chec = curre->next;

	while (curre != NULL && chec->next != NULL
		&& chec->next->next != NULL)
	{
		if (curre == ch)
			return (1);
		curre = curre->next;
		chec = chec->next->next;
	}
	return (0);
}
