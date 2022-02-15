import type { NextPage } from "next"
import {
  Avatar,
  Flex,
  Heading,
  HStack,
  useColorMode,
  VStack,
  useDisclosure,
  Drawer,
  DrawerContent,
  DrawerBody,
  DrawerOverlay,
  DrawerCloseButton,
} from "@chakra-ui/react"
import Sidebar from "../components/profile/Sidebar"
import MobileSidebar from "../components/profile/MobileSidebar"
import MainArea from "../components/profile/MainArea"
import { MdMenu } from "react-icons/md"

const UserPage: NextPage = () => {
  const { colorMode, toggleColorMode } = useColorMode()
  const { isOpen, onOpen, onClose } = useDisclosure()

  return (
    <>
      <HStack w="100vw" h="100vh" overflowX="hidden" align="start" spacing={0}>
        <VStack
          w="290px"
          minH="100vh"
          display={["none", "none", "none", "flex", "flex"]}
        >
          <Sidebar />
        </VStack>
        <VStack flex={1} minH="100vh" p={0} m={0} spacing={0}>
          <Flex
            w="100%"
            h="60px"
            justifyContent="space-between"
            alignItems="center"
            display={["flex", "flex", "flex", "none", "none"]}
            bgColor={colorMode === "light" ? "gray.100" : "gray.700"}
            px={5}
          >
            <HStack spacing={4}>
              <Avatar
                src="avatar-1.jpg"
                border={`4px solid ${
                  colorMode === "light" ? "#F98127" : "#009BFF"
                }`}
              />
              <Heading as="h1" size="md" fontWeight={600}>
                Sandip Sadhukhan
              </Heading>
            </HStack>
            <Flex
              as="button"
              _hover={{
                cursor: "pointer",
              }}
              onClick={onOpen}
            >
              <MdMenu fontSize={30} />
            </Flex>
          </Flex>
          <MainArea />
        </VStack>
      </HStack>
      <Drawer
        isOpen={isOpen}
        placement="left"
        onClose={onClose}
        autoFocus={false}
        returnFocusOnClose={false}
        onOverlayClick={onClose}
        size="full"
      >
        <DrawerCloseButton />
        <DrawerOverlay />
        <DrawerContent w="full">
          <DrawerBody w="full" overflow="hidden">
            <MobileSidebar onClose={onClose} />
          </DrawerBody>
        </DrawerContent>
      </Drawer>
    </>
  )
}

export default UserPage
